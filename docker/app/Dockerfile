FROM python:3.6-slim-stretch

ARG REQUIREMENTS_FILE
ARG DJANGO_SETTINGS_MODULE
ARG RBLOG_SECRET_KEY
ARG SUPERUSER_PASSWORD

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y locales libpq-dev dumb-init && \
    rm -rf /var/lib/apt/lists/*

RUN locale-gen de_DE.UTF-8

COPY ./ /app
WORKDIR /app
RUN pip3 install -r requirements/$REQUIREMENTS_FILE
RUN python3 manage.py collectstatic --ignore=*.scss --noinput

