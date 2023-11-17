@_default:
    just --list

@alex:
	bunx alex README.md

@bootstrap:
    pip install --upgrade pip pip-tools
    pip install --upgrade --requirement requirements.in

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
