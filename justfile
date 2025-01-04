@_default:
    just --list

@alex:
	bunx alex README.md

@bootstrap:
    python -m pip install --upgrade pip uv
    uv pip install --upgrade --requirement pyproject.toml

@build:
    just doctoc
    bundle exec jekyll build

@doctoc:
    bunx doctoc README.md

@down:
    docker compose down

@lint *ARGS:
    # -uv --quiet tool run curlylint _layouts/
    # -bunx awesome-lint README.md
    uv tool run --with pre-commit-uv pre-commit run {{ ARGS }} --all-files

@serve:
    # modd --file=modd.conf
    just up ""

@start *ARGS="--detach":
    just up {{ ARGS }}

@up *ARGS:
    docker compose up {{ ARGS }}
