from kevlar import config
from kevlar.config import ConfigException

from kevlar.log import log


def main():
    try:
        conf = config.from_file('configs/config.cfg')
        log.info('Config: %s', conf)
    except ConfigException:
        log.info('Failed to read config:', exc_info=True)


if __name__ == '__main__':
    main()
