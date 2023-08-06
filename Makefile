.PHONY: setup, enter_container, test, lint, format

setup:
	docker compose down
	docker compose up -d --build

serve:
	docker exec sagemaker_endpoint poetry run serve

enter_container:
	docker exec -it sagemaker_endpoint bash

test:
	docker exec sagemaker_endpoint python3 -m poetry run pytest tests --cov=/var/task --cov-report term-missing

lint:
	docker exec sagemaker_endpoint poetry run mypy --explicit-package-bases .
	docker exec sagemaker_endpoint poetry run ruff check .
	docker exec sagemaker_endpoint poetry run black --check .

format:
	docker exec sagemaker_endpoint poetry run ruff check . --fix --exit-non-zero-on-fix
	docker exec sagemaker_endpoint poetry run black .
