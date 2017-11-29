#!/usr/bin/env bash

docker run --rm \
    -v $(pwd):/home/fenics/shared \
    -w /home/fenics/shared \
    --env HOST_UID=$(id -u) \
    --env HOST_GID=$(id -g) \
    --env PYTHONPATH=/home/fenics/shared \
    quay.io/fenicsproject/stable \
    "python3 -m iceisland"
