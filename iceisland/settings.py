import os

from iceisland.config import Material
from iceisland.units import METER, GRAM, CENTIMETER, GPA, SECOND

g = 9.8 * METER / SECOND ** 2

mesh_dir = os.path.join(
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'meshes'), 'simple_layers'
)

domains = {
    # Bottom sediments
    1: Material(rho=1.5 * GRAM / CENTIMETER ** 3, young_modulus=0.016 * GPA, shear_modulus=0.0054 * GPA),

    # First dense layer
    2: Material(rho=2.1 * GRAM / CENTIMETER ** 3, young_modulus=5.9 * GPA, shear_modulus=2.1 * GPA),

    # Second dense layer
    3: Material(rho=2.5 * GRAM / CENTIMETER ** 3, young_modulus=12.0 * GPA, shear_modulus=4.2 * GPA),

    # Crystal foundation
    4: Material(rho=2.5 * GRAM / CENTIMETER ** 3, young_modulus=37.0 * GPA, shear_modulus=15.6 * GPA),
}
