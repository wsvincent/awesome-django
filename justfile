@_default:
    just --list

@alex:
	npx alex README.md

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
    -npx awesome-lint README.md

@serve:
    # modd --file=modd.conf
    just up ""

@start *ARGS="-d":
    just up {{ ARGS }}

@up *ARGS:
    docker-compose up {{ ARGS }}

@toc:
	npx doctoc README.md
