.PHONY: setup, enter_container, test, lint, format

setup:
	docker compose down
	docker compose up -d --build

enter_container:
	docker exec -it python_app bash

test:
	docker exec python_app python3 -m poetry run pytest tests --cov=/var/task --cov-report term-missing

lint:
	docker exec python_app poetry run mypy --explicit-package-bases .
	docker exec python_app poetry run ruff check .
	docker exec python_app poetry run black --check .

format:
	docker exec python_app poetry run ruff check . --fix --exit-non-zero-on-fix
	docker exec python_app poetry run black .
