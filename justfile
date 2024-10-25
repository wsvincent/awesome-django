@_default:
    just --list

@alex:
	bunx alex README.md

@bootstrap:
    python -m pip install --upgrade pip uv
    python -m uv pip install --upgrade --requirement requirements.in

@build:
    just toc
    bundle exec jekyll build

@down:
    docker-compose down

@lint:
    -curlylint _layouts/
    -bunx awesome-lint README.md

@serve:
    # modd --file=modd.conf
    just up ""

@start *ARGS="--detach":
    just up {{ ARGS }}

@up *ARGS:
    docker-compose up {{ ARGS }}

@toc:
	bunx doctoc README.md
