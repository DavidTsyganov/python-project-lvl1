install:
	@poetry install

lint:
	@poetry run flake8 brain_game

selfcheck:

	@poetry check


check:	selfcheck test lint


build: check

	@poetry build

.PHONY: install test lint selfcheck check build
