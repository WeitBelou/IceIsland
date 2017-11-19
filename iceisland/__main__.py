from dolfin import (
    VectorFunctionSpace, DirichletBC, TrialFunction, TestFunction, Identity, solve, Constant, Function, Expression
)
from dolfin.cpp.function import near
from dolfin.cpp.io import File

from ufl.objects import dx
from ufl.operators import dot, inner, nabla_grad, nabla_div, sym

from iceisland import settings, config
from iceisland.log import log
from iceisland.meshes import create_from_layers


def main():
    c = config.Base(g=settings.g, size=settings.size, layers=settings.layers)
    log.info('Config: %s', c)

    log.info('Generating mesh...')
    mesh = create_from_layers(size=c.size, layers=c.layers)
    mesh.rename('mesh', 'Generated mesh')
    log.info('Mesh generated.')

    filename = 'output/mesh.pvd'
    log.info('Writing mesh to file "{}"'.format(filename))
    File(filename) << mesh
    log.info('Mesh written.')

    V = VectorFunctionSpace(mesh, 'P', 1)
    bc = DirichletBC(V, Constant((0, 0, 0)), lambda x, on_boundary: on_boundary and near(x[2], 0))

    u = TrialFunction(V)
    v = TestFunction(V)

    f = Expression(('0', '0', '-rho*g'), rho=c.rho, g=c.g, degree=3)

    a = inner(c.lambda_ * nabla_div(u) * Identity(3) + 2 * c.mu * sym(nabla_grad(u)), sym(nabla_grad(v))) * dx
    L = dot(f, v) * dx

    u = Function(V)
    solve(a == L, u, bc)

    filename = 'output/displacement.pvd'
    log.info('Writing displacement to file {}...'.format(filename))
    File(filename) << u
    log.info('Displacement written.')


if __name__ == '__main__':
    try:
        main()
    except:
        log.critical('Something happened', exc_info=True)
