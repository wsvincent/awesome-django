TAILWIND_CSS_VERSION := "2.1.1"

@_default:
    just --list

@alex:
	npx alex README.md

@build:
    just toc

@lint:
    npx awesome-lint README.md

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

@serve:
	bundle exec jekyll serve --drafts --watch --port 8000

@toc:
	npx doctoc README.md
