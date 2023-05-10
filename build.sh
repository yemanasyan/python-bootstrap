#!/bin/bash

set -e

project_name="python-bootstrap"
project_volume=${project_name}-volume
docker_sdk_image_name=${project_name}-sdk-image
docker_pipenv_image_name="python-pipenv-image"

################### Functions go after this line ###################

function init() {
    if docker images | awk '{print $1}' | grep -q "^$docker_pipenv_image_name$"; then
        echo "Docker image $docker_pipenv_image_name exists"
    else
        echo "Docker image $docker_pipenv_image_name does not exist. Building one..."
        docker build -t "$docker_pipenv_image_name" -f sdk/Dockerfile sdk/
    fi

    # create a volume that will be used to cache docker builds
    docker volume create "$project_volume" > /dev/null
}

function clean() {
  echo "Cleaning up environment"
  docker volume rm -f "$project_volume"
  docker image rm -f "$docker_pipenv_image_name"
  docker image rm -f "$docker_sdk_image_name"
}

function docker-run() {
  function_name="$1"
  shift

  docker run -it --rm \
      -v .:/project \
      -v $project_volume:/project/.venv \
      --entrypoint "$function_name" \
      "$docker_pipenv_image_name" \
      "$@"
}

function build-sdk() {
  echo "FROM $docker_pipenv_image_name AS builder-linux-x64
COPY Pipfile /project/Pipfile
COPY Pipfile.lock /project/Pipfile.lock
RUN pipenv install --dev" > sdk/sdk.Dockerfile

  docker build -t "$docker_sdk_image_name" -f sdk/sdk.Dockerfile .
}



################### Functions go before this line ###################

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

  if [ "$function_name" != "clean" ] && [ "$function_name" != "init" ]; then
    init
  fi

  $function_name "$@"
else
  # if the function doesn't exists call docker-run and pass all arguments to it
  docker-run "$@"
fi