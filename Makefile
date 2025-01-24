.PHONY: install test lint clean

install:
	pip install -e .[dev]

test:
	pytest -q

lint:
	ruff check .

clean:
	rm -rf build dist *.egg-info .pytest_cache
