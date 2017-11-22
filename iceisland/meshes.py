from typing import List

from dolfin.cpp.mesh import BoxMesh, Point, Mesh

from iceisland.config import Layer, Resolution


def create_from_layers(size: float, resolution: Resolution, layers: List[Layer]) -> Mesh:
    a = size / 2
    h = sum([layer.h for layer in layers])

    return BoxMesh(
        Point(-a, -a, 0), Point(a, a, h),
        resolution.n_x, resolution.n_y, resolution.n_z,
    )
