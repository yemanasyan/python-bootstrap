FROM python:3.10.11-bullseye AS builder-linux-x64
ENV PIPENV_VENV_IN_PROJECT=1

RUN pip install --upgrade pip==20.3.4
RUN pip install pipenv
WORKDIR /project
#VOLUME /project/.venv