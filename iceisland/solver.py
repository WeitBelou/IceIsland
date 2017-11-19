from typing import List

from dolfin.cpp.mesh import Mesh, BoxMesh

from iceisland.config import Base, Layer


def create_layered_mesh(layers: List[Layer]) -> Mesh:
    return BoxMesh(

    )


def solve(config: Base):
    pass
