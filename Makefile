build: toc

.PHONY: alex
alex:
	@npx alex README.md

.PHONY: lint
lint:
	@npx awesome-lint README.md

.PHONY: toc
toc:
	@npx doctoc README.md
