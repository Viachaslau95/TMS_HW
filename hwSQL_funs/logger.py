import logging

LOG_FILE_NAME = 'file.log'


def get_logger():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(funcName)s -  %(message)s  ')
    logfile_handler = logging.FileHandler(filename=LOG_FILE_NAME)
    logfile_handler.setLevel(logging.DEBUG)
    logfile_handler.setFormatter(formatter)

    logger.addHandler(logfile_handler)
    logger.setLevel(logging.DEBUG)
    
    return logger
