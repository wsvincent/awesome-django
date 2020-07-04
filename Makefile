build: toc

.PHONY: alex
alex:
	npx alex README.md

.PHONY: toc
toc:
	npx doctoc README.md
