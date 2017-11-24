#!/usr/bin/env bash

BASENAME=geometry

cd meshes

for m in $(ls); do
    cd ${m}

    gmsh -3 ${BASENAME}.geo

    docker run --rm \
    -v $(pwd):/home/fenics/shared \
    -w /home/fenics/shared \
    --env HOST_UID=$(id -u) \
    --env HOST_GID=$(id -g) \
    --env PYTHONPATH=/home/fenics/shared \
    quay.io/fenicsproject/stable \
    "dolfin-convert ${BASENAME}.msh ${BASENAME}.xml"

    cd ..
done
