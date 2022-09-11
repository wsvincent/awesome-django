@_default:
    just --list

@alex:
	npx alex README.md

@build:
    just toc
    bundle exec jekyll build

@down:
    just down

@lint:
    -curlylint _layouts/
    -npx awesome-lint README.md

@serve:
    # modd --file=modd.conf
    just up ""

@up *ARGS="-d":
    docker-compose up {{ ARGS }}

@toc:
	npx doctoc README.md
