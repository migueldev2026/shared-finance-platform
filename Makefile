.PHONY: install run test lint format docker clean

install:
	python -m pip install -e .

run:
	PYTHONPATH=src python src/main.py

test:
	PYTHONPATH=src python -m pytest

lint:
	python -m ruff check .

format:
	python -m ruff format .

docker:
	docker compose up --build

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache