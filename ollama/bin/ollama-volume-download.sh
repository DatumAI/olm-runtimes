#!/bin/bash

# check model name provided
if [ -z "$1" ]
  then
    echo "No model name supplied e.g. llama2"
    exit 1
fi

MODEL_NAME=$1
mkdir data
mkdir data/$MODEL_NAME

docker run -d --rm \
    --name ollama \
    -v `pwd`/$MODEL_NAME:/root/.ollama \
    ollama/ollama:latest

docker exec -it ollama ollama run $MODEL_NAME
