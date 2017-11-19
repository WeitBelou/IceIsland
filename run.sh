#!/usr/bin/env bash

docker volume create --name instant-cache > /dev/null 2>&1

docker run --rm \
    -v instant-cache:/home/fenics/.instant \
    -v $(pwd):/home/fenics/shared \
    -w /home/fenics/shared \
    --env HOST_UID=$(id -u) \
    --env HOST_GID=$(id -g) \
    --env PYTHONPATH=/home/fenics/shared \
    quay.io/fenicsproject/stable \
    "python3 -m iceisland"
