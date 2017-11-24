import os
import operator as op
from typing import Dict, Callable

from dolfin import Expression, Mesh
from dolfin.cpp.mesh import MeshFunctionSizet


class Material:
    def __init__(self, rho: float, young_modulus: float, shear_modulus: float):
        self._rho = rho
        self._young_modulus = young_modulus
        self._shear_modulus = shear_modulus

    @property
    def rho(self) -> float:
        return self._rho

    @property
    def young_modulus(self) -> float:
        return self._young_modulus

    @property
    def shear_modulus(self) -> float:
        return self._shear_modulus

    @property
    def lambda_(self) -> float:
        return self.shear_modulus * (self.young_modulus - 2 * self.shear_modulus) / (
                3 * self.shear_modulus - self.young_modulus)

    @property
    def mu(self) -> float:
        return self.shear_modulus

    def __repr__(self):
        return '<Material rho={rho} young_modulus={young_modulus} shear_modulus={shear_modulus}>'.format(
            rho=self.rho, young_modulus=self.young_modulus, shear_modulus=self.shear_modulus,
        )


class Base:
    def __init__(self, g: float, mesh_dir: str, materials: Dict[int, Material]):
        self._g = g
        self._mesh_dir = mesh_dir
        self._materials = materials

        self._mesh = Mesh(os.path.join(mesh_dir, 'mesh.xml'))
        self._subdomains = MeshFunctionSizet(os.path.join(mesh_dir, 'mesh_physical_region.xml'))
        self._boundaries = MeshFunctionSizet(os.path.join(mesh_dir, 'mesh_facet_region.xml'))

    @property
    def g(self):
        return self._g

    @property
    def mesh_dir(self) -> str:
        return self._mesh_dir

    @property
    def mesh(self) -> Mesh:
        return self._mesh

    @property
    def materials(self) -> Dict[int, Material]:
        return self._materials

    @property
    def lambda_(self) -> Expression:
        return MaterialGetter(materials=self.materials, subdomains=self._subdomains, f=op.attrgetter('lambda_'))

    @property
    def mu(self) -> Expression:
        return MaterialGetter(materials=self.materials, subdomains=self._subdomains, f=op.attrgetter('mu'))

    @property
    def rho(self):
        return MaterialGetter(materials=self.materials, subdomains=self._subdomains, f=op.attrgetter('rho'))

    def __repr__(self) -> str:
        return '<Base g={g} mesh_dir={mesh_dir} materials={materials}>'.format(
            g=self.g, mesh_dir=self.mesh_dir, materials=self.materials
        )


class UnknownDomainException(Exception):
    pass


class MaterialGetter(Expression):
    def __init__(self, materials: Dict[int, Material], subdomains: MeshFunctionSizet, f: Callable[[Material], float]):
        self._f = f
        self._subdomains = subdomains
        self._materials = materials

        super(MaterialGetter, self).__init__(degree=0)

    def eval_cell(self, values, x, cell):
        material = self._materials.get(self._subdomains[cell.index])
        if material:
            values[0] = self._f(material)
        else:
            raise UnknownDomainException()
