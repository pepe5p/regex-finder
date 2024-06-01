FROM python:3.12-slim-bullseye

MAINTAINER Piotr Karaś <pkaras@student.agh.edu.pl>

RUN apt-get update \
    && apt-get install -y \
    make \
    wget \
    git \
    gcc \
    graphviz \
 	graphviz-dev \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code/

COPY pyproject.toml pyproject.toml

RUN pip install poetry==1.8.2 \
  && poetry config virtualenvs.create false \
  && poetry install --no-root --all-extras

COPY . /code/
