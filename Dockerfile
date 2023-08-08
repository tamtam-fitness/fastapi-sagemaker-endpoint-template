FROM python:3.10

RUN apt-get -y update && apt-get install -y --no-install-recommends \
        g++ \
        make \
        cmake \
        wget \
        nginx \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python & \
    ln -s /usr/bin/pip3 /usr/bin/pip

ENV PATH="/opt/program:${PATH}"
ENV BASE_DIR="/opt/"
ENV PYTHONPATH="/opt/"

RUN pip install poetry==1.5.1
COPY pyproject.toml poetry.lock ./

RUN poetry export --without-hashes --output requirements.txt
RUN pip install -r requirements.txt
COPY ./opt/ /opt/

RUN chmod 755 /opt/program/serve

EXPOSE 8080