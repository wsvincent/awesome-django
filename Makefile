TAILWIND_CSS_VERSION := 1.8.10

build: toc

.PHONY: alex
alex:
	@npx alex README.md

.PHONY: lint
lint:
	@npx awesome-lint README.md

.PHONY: static
static:
	@npx -p tailwindcss@${TAILWIND_CSS_VERSION} tailwindcss build \
		./src/style.css \
		--config ./tailwind.config.js \
		--output ./assets/style.css

.PHONY: serve
serve:
	bundle exec jekyll serve --drafts --watch --port 4000

.PHONY: toc
toc:
	@npx doctoc README.md
