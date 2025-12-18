#!/usr/bin/env -S uv --quiet run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "bs4",
#     "httpx",
#     "pydantic",
#     "python-dateutil",
#     "python-frontmatter",
#     "python-slugify",
#     "pytz",
#     "rich",
#     "typer",
#     "markdown-it-py",
#     "sqlmodel",
# ]
# ///
import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from typing import Optional
from urllib.parse import urlparse

import frontmatter
import httpx
import typer
from bs4 import BeautifulSoup
from bs4 import Tag
from markdown_it import MarkdownIt
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from rich import print
from rich.console import Console
from rich.progress import track
from rich.table import Table
from slugify import slugify
from sqlmodel import Field as SQLField
from sqlmodel import Session
from sqlmodel import SQLModel
from sqlmodel import create_engine
from sqlmodel import select


app = typer.Typer(
    add_help_option=False,
    no_args_is_help=True,
    rich_markup_mode="rich",
)


class Project(BaseModel):
    """Model representing a Django project from the awesome list."""

    model_config = ConfigDict(extra="allow")

    name: str
    description: str
    url: str
    category: str
    slug: str = Field(default="")
    tags: list[str] = Field(default_factory=list)
    github_stars: int | None = None
    github_forks: int | None = None
    github_last_update: str | None = None
    github_last_commit: str | None = None
    previous_urls: list[str] = Field(default_factory=list)

    def __init__(self, **data):
        super().__init__(**data)
        if not self.slug:
            self.slug = slugify(self.name)


# SQLModel database model
class ProjectDB(SQLModel, table=True):
    """SQLModel for storing projects in SQLite database."""

    __tablename__ = "projects"

    id: Optional[int] = SQLField(default=None, primary_key=True)
    name: str = SQLField(index=True)
    description: str
    url: str = SQLField(unique=True)
    category: str = SQLField(index=True)
    slug: str = SQLField(unique=True, index=True)
    tags: str = SQLField(default="[]")  # JSON string
    github_stars: Optional[int] = SQLField(default=None, index=True)
    github_forks: Optional[int] = SQLField(default=None)
    github_last_update: Optional[str] = SQLField(default=None)
    github_last_commit: Optional[str] = SQLField(default=None, index=True)
    previous_urls: str = SQLField(default="[]")  # JSON string

    @classmethod
    def from_project(cls, project: Project) -> "ProjectDB":
        """Convert a Project to ProjectDB."""
        return cls(
            name=project.name,
            description=project.description,
            url=project.url,
            category=project.category,
            slug=project.slug,
            tags=json.dumps(project.tags),
            github_stars=project.github_stars,
            github_forks=project.github_forks,
            github_last_update=project.github_last_update,
            github_last_commit=project.github_last_commit,
            previous_urls=json.dumps(project.previous_urls),
        )

    def to_project(self) -> Project:
        """Convert ProjectDB back to Project."""
        return Project(
            name=self.name,
            description=self.description,
            url=self.url,
            category=self.category,
            slug=self.slug,
            tags=json.loads(self.tags),
            github_stars=self.github_stars,
            github_forks=self.github_forks,
            github_last_update=self.github_last_update,
            github_last_commit=self.github_last_commit,
            previous_urls=json.loads(self.previous_urls),
        )


# Database configuration
DATABASE_PATH = Path("projects.db")
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
console = Console()


def get_engine():
    """Get SQLModel engine."""
    return create_engine(DATABASE_URL, echo=False)


def init_db():
    """Initialize the database and create tables."""
    engine = get_engine()
    SQLModel.metadata.create_all(engine)
    return engine


def parse_project_line(line: Tag, category: str) -> Project | None:
    """Parse a project line from the markdown and return a Project object."""
    try:
        # Find the project link
        link = line.find("a")
        if not link:
            return None

        name = link.text.strip()
        url = link.get("href", "").strip()

        # Get description (text after the link)
        description = line.text.replace(name, "").strip()
        description = re.sub(r"^\s*-\s*", "", description)  # Remove leading dash
        description = re.sub(r"^\s*", "", description)  # Remove leading whitespace

        if not all([name, url, description]):
            return None

        return Project(name=name, description=description, url=url, category=category)
    except Exception as e:
        print(f"[red]Error parsing project line: {e}[/red]")
        return None


def read_readme(file_path: Path) -> str:
    """Read README content from local file and convert to HTML."""
    markdown_content = file_path.read_text()
    md = MarkdownIt()
    html_content = md.render(markdown_content)
    return html_content


def parse_readme(content: str) -> list[Project]:
    """Parse README content and extract projects."""
    soup = BeautifulSoup(content, "html.parser")
    projects = []
    current_category = ""

    for element in soup.find_all(["h2", "h3", "li"]):
        if element.name in ["h2", "h3"]:
            current_category = element.text.strip()
        elif element.name == "li" and current_category:
            if current_category == "Contents":
                continue

            project = parse_project_line(element, current_category)
            if project:
                projects.append(project)

    return projects


def merge_project_data(existing: dict[str, Any], new: dict[str, Any]) -> dict[str, Any]:
    """
    Merge existing project data with new data, preserving existing values
    while updating with new information where appropriate.
    """
    # Start with the existing data
    merged = existing.copy()

    # Always update core fields from the README
    core_fields = {"name", "url", "category"}
    for field in core_fields:
        if field in new:
            # If URL is changing, store the old URL in previous_urls
            if field == "url" and new["url"] != existing.get("url"):
                previous_urls = merged.get("previous_urls", [])
                old_url = existing.get("url")
                if old_url and old_url not in previous_urls:
                    previous_urls.append(old_url)
                merged["previous_urls"] = previous_urls
            merged[field] = new[field]

    # Smart merge for description - update only if meaningfully different
    if "description" in new and new["description"] != existing.get("description", ""):
        merged["description"] = new["description"]

    # Update GitHub metrics if they exist in new data
    github_fields = {"github_stars", "github_forks", "github_last_update", "github_last_commit"}
    for field in github_fields:
        if field in new and new[field] is not None:
            merged[field] = new[field]

    return merged


def save_project(project: Project, output_dir: Path):
    """Save project as a markdown file with frontmatter, preserving and merging existing content."""
    output_file = output_dir / f"{project.slug}.md"
    project_data = project.model_dump(exclude_none=True)

    if output_file.exists():
        try:
            # Load existing file
            existing_post = frontmatter.load(output_file)
            existing_data = dict(existing_post.metadata)

            # Merge data, favoring preservation of existing content
            merged_data = merge_project_data(existing_data, project_data)

            # Create new post with merged data but keep existing content
            post = frontmatter.Post(existing_post.content, **merged_data)
        except Exception as e:
            print(
                f"[yellow]Warning: Could not load existing file {output_file}, creating new: {e}[/yellow]"
            )
            post = frontmatter.Post(project.description, **project_data)
    else:
        # Create new file
        post = frontmatter.Post(project.description, **project_data)

    output_file.write_text(frontmatter.dumps(post))


def extract_github_info(url: str) -> dict[str, str] | None:
    """Extract owner and repo from a GitHub URL."""
    parsed = urlparse(url)
    if parsed.netloc != "github.com":
        return None

    parts = parsed.path.strip("/").split("/")
    if len(parts) >= 2:
        return {"owner": parts[0], "repo": parts[1]}
    return None


def get_github_metrics(
    owner: str, repo: str, client: httpx.Client
) -> tuple[dict, str | None]:
    """
    Fetch GitHub metrics for a repository.
    Returns a tuple of (metrics_dict, new_url) where new_url is set if the repo has moved.
    """
    headers = {}
    if github_token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"token {github_token}"

    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        response = client.get(
            api_url,
            headers=headers,
            timeout=10.0,
            follow_redirects=True,  # Enable following redirects
        )

        # Check if we followed a redirect
        new_url = None
        if len(response.history) > 0:
            for r in response.history:
                if r.status_code == 301:
                    # Get the new location from the API response
                    data = response.json()
                    new_url = data.get("html_url")
                    if new_url:
                        print(
                            f"[yellow]Repository moved: {owner}/{repo} -> {new_url}[/yellow]"
                        )
                    break

        response.raise_for_status()
        data = response.json()

        metrics = {
            "github_stars": data["stargazers_count"],
            "github_forks": data["forks_count"],
            "github_last_update": data["updated_at"],
        }

        # Fetch last commit date
        commits_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        try:
            commits_response = client.get(
                commits_url,
                headers=headers,
                params={"per_page": 1},
                timeout=10.0,
                follow_redirects=True,
            )
            commits_response.raise_for_status()
            commits_data = commits_response.json()
            if commits_data and len(commits_data) > 0:
                metrics["github_last_commit"] = commits_data[0]["commit"]["committer"]["date"]
        except httpx.HTTPError as e:
            print(f"[yellow]Warning: Could not fetch commits for {owner}/{repo}: {str(e)}[/yellow]")

        return metrics, new_url

    except httpx.HTTPError as e:
        print(f"[red]Error fetching GitHub metrics for {owner}/{repo}: {str(e)}[/red]")
        return {}, None


def load_project(file_path: Path) -> Project | None:
    """Load a project from a markdown file."""
    try:
        post = frontmatter.load(file_path)
        return Project(**post.metadata)
    except Exception as e:
        print(f"[red]Error loading project from {file_path}: {str(e)}[/red]")
        return None


@app.command()
def parse(readme_path: Path = Path("README.md"), output_dir: str = "_projects"):
    """
    Parse local Awesome Django README and create individual project files with frontmatter.
    Preserves existing file content and metadata while updating with new information from README.
    """
    if not readme_path.exists():
        print(f"[red]Error: README file not found at {readme_path}[/red]")
        raise typer.Exit(1)

    print(f"[bold blue]Reading README from {readme_path}...[/bold blue]")

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Read and parse README
    content = read_readme(readme_path)
    projects = parse_readme(content)

    print(f"[green]Found {len(projects)} projects[/green]")

    # Save individual project files
    for project in projects:
        save_project(project, output_path)
        print(f"[green]Updated {project.name} in {project.slug}.md[/green]")


@app.command()
def update_metrics(projects_dir: Path = Path("_projects"), batch_size: int = 50):
    """
    Update GitHub metrics (stars, forks, last update) for all projects.
    """
    if not projects_dir.exists():
        print(f"[red]Error: Projects directory not found at {projects_dir}[/red]")
        raise typer.Exit(1)

    print(
        f"[bold blue]Updating GitHub metrics for projects in {projects_dir}...[/bold blue]"
    )

    # Load all projects
    project_files = list(projects_dir.glob("*.md"))
    projects = []
    for file in project_files:
        if project := load_project(file):
            projects.append((file, project))

    print(f"[green]Found {len(projects)} projects to update[/green]")

    # Update metrics in batches to avoid rate limiting
    with httpx.Client() as client:
        for i in track(
            range(0, len(projects), batch_size), description="Updating projects"
        ):
            batch = projects[i : i + batch_size]
            for file_path, project in batch:
                if github_info := extract_github_info(project.url):
                    metrics, new_url = get_github_metrics(
                        github_info["owner"], github_info["repo"], client
                    )

                    if metrics:
                        # Update project with new metrics
                        for key, value in metrics.items():
                            setattr(project, key, value)

                        # Update URL if repository has moved
                        if new_url and new_url != project.url:
                            # Store the old URL in previous_urls
                            if not hasattr(project, "previous_urls"):
                                project.previous_urls = []
                            project.previous_urls.append(project.url)
                            # Update to new URL
                            project.url = new_url
                            print(
                                f"[yellow]Updated URL for {project.name}: {project.url}[/yellow]"
                            )

                        save_project(project, projects_dir)
                        print(f"[green]Updated metrics for {project.name}[/green]")

    print("[bold blue]Finished updating GitHub metrics![/bold blue]")


@app.command()
def sync_db(projects_dir: Path = Path("_projects")):
    """
    Sync projects from markdown files to SQLite database.
    """
    if not projects_dir.exists():
        print(f"[red]Error: Projects directory not found at {projects_dir}[/red]")
        raise typer.Exit(1)

    print(f"[bold blue]Syncing projects to {DATABASE_PATH}...[/bold blue]")

    engine = init_db()

    # Load all projects from markdown files
    project_files = list(projects_dir.glob("*.md"))
    projects_loaded = 0

    with Session(engine) as session:
        # Clear existing data
        session.exec(select(ProjectDB)).all()
        for existing in session.exec(select(ProjectDB)).all():
            session.delete(existing)
        session.commit()

        # Load new data
        for file in track(project_files, description="Loading projects"):
            if project := load_project(file):
                db_project = ProjectDB.from_project(project)
                session.add(db_project)
                projects_loaded += 1

        session.commit()

    print(f"[green]Synced {projects_loaded} projects to {DATABASE_PATH}[/green]")


@app.command()
def query(
    category: Optional[str] = typer.Option(None, "--category", "-c", help="Filter by category"),
    min_stars: Optional[int] = typer.Option(None, "--min-stars", "-s", help="Minimum GitHub stars"),
    limit: int = typer.Option(20, "--limit", "-l", help="Maximum results to show"),
    sort_by: str = typer.Option("stars", "--sort", help="Sort by: stars, name, commits"),
):
    """
    Query projects from the database with filters.
    """
    if not DATABASE_PATH.exists():
        print("[red]Database not found. Run 'sync-db' first.[/red]")
        raise typer.Exit(1)

    engine = get_engine()

    with Session(engine) as session:
        statement = select(ProjectDB)

        if category:
            statement = statement.where(ProjectDB.category == category)

        if min_stars:
            statement = statement.where(ProjectDB.github_stars >= min_stars)

        # Sorting
        if sort_by == "stars":
            statement = statement.order_by(ProjectDB.github_stars.desc())
        elif sort_by == "name":
            statement = statement.order_by(ProjectDB.name)
        elif sort_by == "commits":
            statement = statement.order_by(ProjectDB.github_last_commit.desc())

        statement = statement.limit(limit)
        results = session.exec(statement).all()

        if not results:
            print("[yellow]No projects found matching criteria.[/yellow]")
            return

        table = Table(title=f"Projects ({len(results)} results)")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Category", style="green")
        table.add_column("Stars", justify="right", style="yellow")
        table.add_column("Last Commit", style="magenta")

        for p in results:
            stars = str(p.github_stars) if p.github_stars else "-"
            last_commit = p.github_last_commit[:10] if p.github_last_commit else "-"
            table.add_row(p.name, p.category, stars, last_commit)

        console.print(table)


@app.command()
def top(
    limit: int = typer.Option(20, "--limit", "-l", help="Number of projects to show"),
    category: Optional[str] = typer.Option(None, "--category", "-c", help="Filter by category"),
):
    """
    Show top projects by GitHub stars.
    """
    if not DATABASE_PATH.exists():
        print("[red]Database not found. Run 'sync-db' first.[/red]")
        raise typer.Exit(1)

    engine = get_engine()

    with Session(engine) as session:
        statement = select(ProjectDB).where(ProjectDB.github_stars.isnot(None))

        if category:
            statement = statement.where(ProjectDB.category == category)

        statement = statement.order_by(ProjectDB.github_stars.desc()).limit(limit)
        results = session.exec(statement).all()

        table = Table(title=f"Top {len(results)} Projects by Stars")
        table.add_column("#", justify="right", style="dim")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Category", style="green")
        table.add_column("Stars", justify="right", style="yellow")
        table.add_column("Forks", justify="right", style="blue")
        table.add_column("URL", style="dim")

        for i, p in enumerate(results, 1):
            table.add_row(
                str(i),
                p.name,
                p.category,
                f"{p.github_stars:,}",
                str(p.github_forks or "-"),
                p.url[:50] + "..." if len(p.url) > 50 else p.url,
            )

        console.print(table)


@app.command()
def categories():
    """
    List all categories with project counts.
    """
    if not DATABASE_PATH.exists():
        print("[red]Database not found. Run 'sync-db' first.[/red]")
        raise typer.Exit(1)

    engine = get_engine()

    with Session(engine) as session:
        results = session.exec(select(ProjectDB)).all()

        # Count by category
        category_counts: dict[str, int] = {}
        category_stars: dict[str, int] = {}
        for p in results:
            category_counts[p.category] = category_counts.get(p.category, 0) + 1
            category_stars[p.category] = category_stars.get(p.category, 0) + (p.github_stars or 0)

        # Sort by count
        sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)

        table = Table(title="Categories")
        table.add_column("Category", style="cyan")
        table.add_column("Projects", justify="right", style="green")
        table.add_column("Total Stars", justify="right", style="yellow")

        for cat, count in sorted_categories:
            table.add_row(cat, str(count), f"{category_stars[cat]:,}")

        console.print(table)
        print(f"\n[bold]Total: {len(sorted_categories)} categories, {len(results)} projects[/bold]")


@app.command()
def search(
    query: str = typer.Argument(..., help="Search term"),
    limit: int = typer.Option(20, "--limit", "-l", help="Maximum results"),
):
    """
    Search projects by name or description.
    """
    if not DATABASE_PATH.exists():
        print("[red]Database not found. Run 'sync-db' first.[/red]")
        raise typer.Exit(1)

    engine = get_engine()
    query_lower = query.lower()

    with Session(engine) as session:
        results = session.exec(select(ProjectDB)).all()

        # Filter by search term
        matches = [
            p for p in results
            if query_lower in p.name.lower() or query_lower in p.description.lower()
        ]

        # Sort by stars
        matches.sort(key=lambda x: x.github_stars or 0, reverse=True)
        matches = matches[:limit]

        if not matches:
            print(f"[yellow]No projects found matching '{query}'[/yellow]")
            return

        table = Table(title=f"Search results for '{query}' ({len(matches)} matches)")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Category", style="green")
        table.add_column("Stars", justify="right", style="yellow")
        table.add_column("Description", style="dim", max_width=50)

        for p in matches:
            stars = str(p.github_stars) if p.github_stars else "-"
            desc = p.description[:50] + "..." if len(p.description) > 50 else p.description
            table.add_row(p.name, p.category, stars, desc)

        console.print(table)


@app.command()
def stale(
    days: int = typer.Option(365, "--days", "-d", help="Days since last commit to consider stale"),
    limit: int = typer.Option(30, "--limit", "-l", help="Maximum results"),
):
    """
    Find stale/unmaintained projects (no commits in X days).
    """
    if not DATABASE_PATH.exists():
        print("[red]Database not found. Run 'sync-db' first.[/red]")
        raise typer.Exit(1)

    engine = get_engine()
    cutoff = datetime.now().replace(tzinfo=None)

    with Session(engine) as session:
        results = session.exec(
            select(ProjectDB).where(ProjectDB.github_last_commit.isnot(None))
        ).all()

        # Filter stale projects
        stale_projects = []
        for p in results:
            try:
                last_commit = datetime.fromisoformat(p.github_last_commit.replace("Z", "+00:00"))
                last_commit = last_commit.replace(tzinfo=None)
                days_since = (cutoff - last_commit).days
                if days_since >= days:
                    stale_projects.append((p, days_since))
            except (ValueError, AttributeError):
                continue

        # Sort by oldest first
        stale_projects.sort(key=lambda x: x[1], reverse=True)
        stale_projects = stale_projects[:limit]

        if not stale_projects:
            print(f"[green]No stale projects found (>{days} days without commits)[/green]")
            return

        table = Table(title=f"Stale Projects (no commits in {days}+ days)")
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Category", style="green")
        table.add_column("Stars", justify="right", style="yellow")
        table.add_column("Last Commit", style="red")
        table.add_column("Days Ago", justify="right", style="red")

        for p, days_ago in stale_projects:
            stars = str(p.github_stars) if p.github_stars else "-"
            last_commit = p.github_last_commit[:10] if p.github_last_commit else "-"
            table.add_row(p.name, p.category, stars, last_commit, str(days_ago))

        console.print(table)
        print(f"\n[bold red]Found {len(stale_projects)} stale projects[/bold red]")


@app.command()
def stats():
    """
    Show database statistics.
    """
    if not DATABASE_PATH.exists():
        print("[red]Database not found. Run 'sync-db' first.[/red]")
        raise typer.Exit(1)

    engine = get_engine()

    with Session(engine) as session:
        all_projects = session.exec(select(ProjectDB)).all()
        github_projects = [p for p in all_projects if p.github_stars is not None]

        total_stars = sum(p.github_stars or 0 for p in all_projects)
        categories = set(p.category for p in all_projects)

        print("\n[bold blue]Database Statistics[/bold blue]")
        print(f"  Total projects: [green]{len(all_projects)}[/green]")
        print(f"  GitHub projects: [green]{len(github_projects)}[/green]")
        print(f"  Categories: [green]{len(categories)}[/green]")
        print(f"  Total stars: [yellow]{total_stars:,}[/yellow]")

        if github_projects:
            avg_stars = total_stars / len(github_projects)
            max_stars_project = max(github_projects, key=lambda x: x.github_stars or 0)
            print(f"  Average stars: [yellow]{avg_stars:.0f}[/yellow]")
            print(f"  Most starred: [cyan]{max_stars_project.name}[/cyan] ({max_stars_project.github_stars:,} stars)")


if __name__ == "__main__":
    app()
