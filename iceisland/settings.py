import os

from iceisland.config import Material
from iceisland.units import METER, GRAM, CENTIMETER, GPA, SECOND

g = 9.8 * METER / SECOND ** 2

_MESHES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meshes')

mesh_dir = os.path.join(_MESHES_DIR, 'simple_layers')

BOTTOM_SEDIMENTS = 1
FIRST_DENSE_LAYER = 2
SECOND_DENSE_LAYER = 3
CRYSTAL_FOUNDATION = 4

domains = {
    BOTTOM_SEDIMENTS: Material(rho=1.5 * GRAM / CENTIMETER ** 3, young_modulus=0.016 * GPA, shear_modulus=0.0054 * GPA),
    FIRST_DENSE_LAYER: Material(rho=2.1 * GRAM / CENTIMETER ** 3, young_modulus=5.9 * GPA, shear_modulus=2.1 * GPA),
    SECOND_DENSE_LAYER: Material(rho=2.5 * GRAM / CENTIMETER ** 3, young_modulus=12.0 * GPA, shear_modulus=4.2 * GPA),
    CRYSTAL_FOUNDATION: Material(rho=2.5 * GRAM / CENTIMETER ** 3, young_modulus=37.0 * GPA, shear_modulus=15.6 * GPA),
}
