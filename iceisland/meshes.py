from typing import List

from dolfin.cpp.mesh import BoxMesh, Point, Mesh

from iceisland.config import Layer


def create_from_layers(size: float, layers: List[Layer]) -> Mesh:
    a = size / 2
    h = sum([layer.h for layer in layers])

    n_x = n_y = 10
    n_z = 5 * n_x

    return BoxMesh(
        Point(-a, -a, 0), Point(a, a, h),
        n_x, n_y, n_z,
    )
