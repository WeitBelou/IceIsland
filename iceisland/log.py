import logging

log = logging.getLogger('ice_island')


def _init_logger():
    formatter = logging.Formatter('[%(levelname)s] [%(asctime)s]  %(message)s')

    file = logging.FileHandler('ice_island.log',)
    file.setLevel(logging.INFO)
    file.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    log.addHandler(console)
    log.addHandler(file)

    log.setLevel(logging.INFO)


_init_logger()
