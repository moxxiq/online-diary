FROM python:3.10-slim-bullseye

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /backend/requirements.txt

RUN apt-get update && \
  pip install --upgrade pip && \
  apt install --no-install-recommends gcc -y && \
  rm -rf /var/lib/apt/lists/*

COPY . /backend/
RUN pip install -r requirements.txt