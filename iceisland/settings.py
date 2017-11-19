from iceisland.config import Layer
from iceisland.units import METER, GRAM, CENTIMETER, GPA, KILOMETER, SECOND

g = 9.8 * METER / SECOND ** 2

size = 1 * KILOMETER

layers = [
    # Crystal foundation
    Layer(h=1.0 * KILOMETER, rho=2.5 * GRAM / CENTIMETER ** 3, young_modulus=37.0 * GPA, shear_modulus=15.6 * GPA),

    # SECOND dense layer
    Layer(h=400 * METER, rho=2.5 * GRAM / CENTIMETER ** 3, young_modulus=12.0 * GPA, shear_modulus=4.2 * GPA),

    # First dense layer
    Layer(h=300 * METER, rho=2.1 * GRAM / CENTIMETER ** 3, young_modulus=5.9 * GPA, shear_modulus=2.1 * GPA),

    # Bottom sediments
    Layer(h=50 * METER, rho=1.5 * GRAM / CENTIMETER ** 3, young_modulus=0.016 * GPA, shear_modulus=0.0054 * GPA),
]
