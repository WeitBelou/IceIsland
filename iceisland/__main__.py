from dolfin import (
    VectorFunctionSpace, DirichletBC, TrialFunction, TestFunction, Identity, solve, Constant, Function, Expression,
    FunctionSpace, project, Mesh
)
from dolfin.cpp.function import near

from ufl.objects import dx, ds
from ufl.operators import dot, inner, nabla_grad, nabla_div, sym, tr, sqrt

from iceisland import settings, config
from iceisland.io import write
from iceisland.log import log
from iceisland.meshes import create_from_layers

_c = config.Base(g=settings.g, size=settings.size, layers=settings.layers)


def sigma(u):
    return _c.lambda_ * nabla_div(u) * Identity(3) + 2 * _c.mu * sym(nabla_grad(u))


def solve_elasticity(mesh: Mesh) -> Function:
    V = VectorFunctionSpace(mesh, 'P', 1)
    bc = DirichletBC(V, Constant((0, 0, 0)), lambda x, on_boundary: on_boundary and near(x[2], 0))

    u = TrialFunction(V)
    v = TestFunction(V)

    f = Expression(('0', '0', '-rho*g'), rho=_c.rho, g=_c.g, degree=3)
    T = Constant((0, 0, 0))

    a = inner(sigma(u), sym(nabla_grad(v))) * dx
    L = dot(f, v) * dx + dot(T, v) * ds

    u = Function(V)
    solve(a == L, u, bc)

    return u


def compute_stress(mesh: Mesh, displacement: Function) -> Function:
    V = FunctionSpace(mesh, 'P', 1)
    s = sigma(displacement) - tr(sigma(displacement)) * Identity(3) / 3
    return project(sqrt(1.5 * inner(s, s)), V)


def main():
    log.info('Config: %s', _c)

    mesh = create_from_layers(size=_c.size, layers=_c.layers)
    write('mesh', mesh)

    u = solve_elasticity(mesh)
    write('displacement', u)

    stress = compute_stress(mesh, u)
    write('stress', stress)


if __name__ == '__main__':
    try:
        main()
    except:
        log.critical('Something happened', exc_info=True)
