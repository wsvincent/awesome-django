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
# ]
# ///
import os
import re
from pathlib import Path
from typing import Any
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
from rich.progress import track
from slugify import slugify


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
    previous_urls: list[str] = Field(default_factory=list)

    def __init__(self, **data):
        super().__init__(**data)
        if not self.slug:
            self.slug = slugify(self.name)


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
    github_fields = {"github_stars", "github_forks", "github_last_update"}
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

        return {
            "github_stars": data["stargazers_count"],
            "github_forks": data["forks_count"],
            "github_last_update": data["updated_at"],
        }, new_url

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


if __name__ == "__main__":
    app()
