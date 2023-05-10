#!/bin/bash

set -e

project_name="python-bootstrap"
docker_image_name="python-pip-image"

if [ "$1" != "clean" ]; then
  if docker images | awk '{print $1}' | grep -q "^$docker_image_name$"; then
      echo "Docker image $1 exists"
  else
      echo "Docker image $1 does not exist. Building one..."
      docker build -t "$docker_image_name" -f sdk/Dockerfile sdk/
  fi
fi

# create a volume that will be used to cache docker builds
docker volume create "$project_name" > /dev/null

function clean() {
  echo "Cleaning up environment"
  docker volume rm -f "$project_name"
  docker image rm -f "$docker_image_name"
}

function docker-run() {
  function_name="$1"
  shift

  docker run -it --rm \
      -v .:/project \
      -v $project_name:/root/.local/share/virtualenvs/ \
      --workdir /project \
      --entrypoint "$function_name" \
      "$docker_image_name" \
      "$@"
}

function pipenv-install() {
  docker-run pipenv install
}

function pipenv-install-dev() {
  docker-run pipenv install --dev
}

function setup-sdk() {
  pipenv-install-dev

  echo "version: '3.8'
services:
  ${project_name}-sdk:
    image: $docker_image_name
    working_dir: /project
    volumes:
      - $(pwd):/project
      - $project_name:/root/.local/share/virtualenvs/
volumes:
  $project_name:" \ > sdk/docker-compose.yml
}

if [ $# -eq 0 ]; then
  echo "No arguments provided, please provide a function name."
  exit 1
fi

# Consider the first argument as function name and check if it exists.
function_name="$1"
if declare -F "$function_name" > /dev/null; then
  # if the function exists call shift to remove the first argument (function name) from the arguments list and
  # pass the reaming ones as arguments
  shift
  $function_name "$@"
else
  # if the function doesn't exists call docker-run and pass all arguments to it
  docker-run "$@"
fi