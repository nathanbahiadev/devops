FROM python:3.10-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements/requirements.txt ./requirements/requirements.txt

RUN pip install -r ./requirements/requirements.txt

COPY . .
