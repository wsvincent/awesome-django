# Default recipe - lists all available recipes
@_default:
    just --list

# Run alex linter on README.md to find inconsiderate writing
@alex:
	bunx alex README.md

# Install and update dependencies
@bootstrap:
    python -m pip install --upgrade pip uv
    uv pip install --upgrade --requirement pyproject.toml

# Generate table of contents and build the Jekyll site
@build:
    just doctoc
    bundle exec jekyll build

# Generate table of contents for README.md
@doctoc:
    bunx doctoc README.md

# Stop the Docker containers
@down:
    docker compose down

# Run linting on all files
@lint *ARGS:
    # -uv --quiet tool run curlylint _layouts/
    # -bunx awesome-lint README.md
    uv tool run --with pre-commit-uv pre-commit run {{ ARGS }} --all-files

# Start local development server
@serve:
    # modd --file=modd.conf
    just up ""

# Start containers (detached by default)
@start *ARGS="--detach":
    just up {{ ARGS }}

# Start Docker containers with optional arguments
@up *ARGS:
    docker compose up {{ ARGS }}
