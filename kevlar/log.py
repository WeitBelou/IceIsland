import logging

log = logging.getLogger('kevlar')


def _init_logger():
    file = logging.FileHandler('kevlar.log')
    file.setLevel(logging.INFO)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    log.addHandler(console)
    log.addHandler(file)

    log.setLevel(logging.INFO)


_init_logger()
