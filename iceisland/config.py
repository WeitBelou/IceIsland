class Mesh:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def __str__(self) -> str:
        return '<Mesh radius={radius}>'.format(radius=self.radius)


class Material:
    def __init__(self, density: float, young_modulus: float, shear_modulus: float):
        self._density = density

        self._young_modulus = young_modulus
        self._shear_modulus = shear_modulus

    @property
    def density(self):
        return self._density

    @property
    def young_modulus(self):
        return self._young_modulus

    @property
    def shear_modulus(self):
        return self._shear_modulus

    def __str__(self) -> str:
        return '<Material density={density} young_modulus={young_modulus} shear_modulus={shear_modulus}>'.format(
            density=self.density, young_modulus=self.young_modulus, shear_modulus=self.shear_modulus
        )


class Base:
    def __init__(self, mesh: Mesh, material: Material):
        self._mesh = mesh
        self._material = material

    @property
    def mesh(self) -> Mesh:
        return self._mesh

    @property
    def material(self) -> Material:
        return self._material

    def __str__(self) -> str:
        return '<Base mesh={mesh} material={material}>'.format(
            mesh=self.mesh, material=self.material
        )


class ConfigException(Exception):
    pass


def from_file(path: str) -> Base:
    from configparser import ConfigParser, NoOptionError

    parser = ConfigParser()

    files_read = parser.read(path)
    if len(files_read) != 1 or files_read[0] != path:
        raise ConfigException()

    default_section = parser.default_section

    try:
        mesh = Mesh(radius=parser.getfloat(default_section, 'mesh.radius'))
    except NoOptionError as e:
        raise ConfigException(e)

    try:
        material = Material(
            density=parser.getfloat(default_section, 'material.density'),
            young_modulus=parser.getfloat(default_section, 'material.young_modulus'),
            shear_modulus=parser.getfloat(default_section, 'material.shear_modulus'),
        )
    except NoOptionError as e:
        raise ConfigException(e)

    c = Base(mesh=mesh, material=material)
    return c
