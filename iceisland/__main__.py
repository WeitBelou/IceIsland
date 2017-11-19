import sys

from iceisland import solver, settings, config
from iceisland.log import log


def main():
    conf = config.Base(layers=settings.layers)
    log.info('Config: %s', conf)

    try:
        solver.solve(conf)
    except Exception:
        log.error('Can not solve problem:', exc_inf=True)
        sys.exit(-2)


if __name__ == '__main__':
    main()
