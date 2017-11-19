from iceisland import config, solver
from iceisland.config import ConfigException

from iceisland.log import log


def main():
    try:
        conf = config.from_file('configs/config.cfg')
        log.info('Config: %s', conf)
    except ConfigException:
        log.error('Failed to read config:', exc_info=True)
        exit(1)

    solver.solve(conf)


if __name__ == '__main__':
    main()
