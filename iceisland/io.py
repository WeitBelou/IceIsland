import os
from typing import Union

from dolfin import Function
from dolfin.cpp.io import File
from ufl import Mesh

from iceisland.log import log

OUTPUT_DIR = 'output'


def write(name: str, data: Union[Function, Mesh]):
    filename = os.path.join(OUTPUT_DIR, '{}.pvd'.format(name))
    log.info('Writing {name} to file "{filename}"'.format(name=name, filename=filename))
    File(filename) << data
    log.info('{} written.'.format(name))
