FROM python:3.10-buster
RUN pip install poetry==1.5.1
COPY pyproject.toml poetry.lock ./app/
WORKDIR /app
RUN poetry export --without-hashes --output requirements.txt
RUN pip install -r requirements.txt
COPY . ./app/
