from typing import List

from dolfin import Expression


class Layer:
    """"""

    def __init__(self, h: float, rho: float, young_modulus: float, shear_modulus: float):
        self._h = h
        self._rho = rho
        self._young_modulus = young_modulus
        self._shear_modulus = shear_modulus

    @property
    def h(self) -> float:
        return self._h

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
        return '<Layer h={h} rho={rho} young_modulus={young_modulus} shear_modulus={shear_modulus}>'.format(
            h=self.h, rho=self.rho,
            young_modulus=self.young_modulus, shear_modulus=self.shear_modulus,
        )


class Base:
    def __init__(self, g: float, size: float, layers: List[Layer]):
        self._g = g
        self._size = size
        self._layers = layers

    @property
    def layers(self) -> List[Layer]:
        return self._layers

    @property
    def size(self):
        return self._size

    @property
    def g(self):
        return self._g

    @property
    def lambda_(self) -> Expression:
        class Lambda(Expression):
            def eval(self, value, x):
                h = 0
                for layer in self.layers:
                    h += layer.h
                    if x[2] <= h:
                        value[0] = layer.lambda_
                        return

        return Lambda(degree=0)

    @property
    def mu(self) -> Expression:

        class Mu(Expression):
            def eval(self, value, x):
                h = 0
                for layer in self.layers:
                    h += layer.h
                    if x[2] <= h:
                        value[0] = layer.mu
                        return

        return Mu(degree=0)

    @property
    def rho(self):

        class Rho(Expression):
            def eval(self, value, x):
                h = 0
                for layer in self.layers:
                    h += layer.h
                    if x[2] <= h:
                        value[0] = layer.rho
                        return

        return Rho(degree=0)

    def __repr__(self) -> str:
        return '<Base g={g} size={size} layers={layers}>'.format(
            g=self.g, size=self.size,
            layers=self.layers
        )
