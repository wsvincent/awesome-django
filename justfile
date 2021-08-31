@_default:
    just --list

@alex:
	npx alex README.md

@build:
    just toc
    bundle exec jekyll build

@lint:
    -curlylint _layouts/
    -npx awesome-lint README.md

@serve:
    modd --file=modd.conf
    bundle exec jekyll serve --drafts --watch --port 8000

@toc:
	npx doctoc README.md
