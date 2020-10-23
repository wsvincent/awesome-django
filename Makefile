TAILWIND_CSS_VERSION := 1.9.2

build: toc

.PHONY: alex
alex:
	@npx alex README.md

.PHONY: lint
lint:
	@npx awesome-lint README.md

.PHONY: static
static:
	@JEKYLL_ENV=production \
		npx -p tailwindcss@${TAILWIND_CSS_VERSION} tailwindcss build \
			./src/style.css \
			--config ./tailwind.config.js \
			--output ./assets/style.css

	@npx -p tailwindcss@${TAILWIND_CSS_VERSION} tailwindcss build \
		./src/style.css \
		--config ./tailwind.config.js \
		--output ./assets/development.css

.PHONY: serve
serve:
	@bundle exec jekyll serve --drafts --watch --port 8000

.PHONY: toc
toc:
	@npx doctoc README.md
