TAILWIND_CSS_VERSION := "2.1.1"

@_default:
    just --list

@alex:
	npx alex README.md

@build:
    just toc
    bundle exec jekyll build

@lint:
    npx awesome-lint README.md
@serve:
    modd --file=modd.conf
    bundle exec jekyll serve --drafts --watch --port 8000

@static:
	JEKYLL_ENV=production \
	npx -p tailwindcss@{{TAILWIND_CSS_VERSION}} tailwindcss build \
		./src/style.css \
		--config ./tailwind.config.js \
		--output ./assets/style.css

	npx -p tailwindcss@{{TAILWIND_CSS_VERSION}} tailwindcss build \
		./src/style.css \
		--config ./tailwind.config.js \
		--output ./assets/development.css \
		-w

@toc:
	npx doctoc README.md
