FROM python:3.10-slim-buster

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
  pip install --upgrade pip && \
  apt install --no-install-recommends gcc -y && \
  rm -rf /var/lib/apt/lists/*
COPY ./*.py requirements.txt /backend/
RUN pip install -r requirements.txt