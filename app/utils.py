import logging


def get_logger(name: str, level=logging.INFO):
    log_format = '%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s()] [%(levelname)s] %(message)s'
    logging.basicConfig(format=log_format)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger
