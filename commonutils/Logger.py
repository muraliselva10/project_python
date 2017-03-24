__author__ = 'muralidharan'

import logging
from project_python.commonutils.Singleton import Singleton


class Logger(object):
    """
    Logger class for Backup/restore script execution
    log file will be generated for the given path for the given log level.
    This class is mapped as singleton class , same logger instance for
    all the classes
    """
    __metaclass__ = Singleton

    def __init__(self):
        self.__logger = logging.getLogger()
        logging.getLogger("our_log").setLevel(logging.WARNING)

    def set_log_file(self, log_file):
        """
        set log file to be generated for logging
        formatter - timestamp, level name , class , function name , line no , message
        :param log_file: log file path
        """
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('[%(asctime)s :%(levelname)s|%(filename)s:%(funcName)s:%(lineno)d] %(message)s')
        file_handler.setFormatter(formatter)
        self.__logger.addHandler(file_handler)

    def set_log_level(self, log_level):
        """
        As per the user input, set the log level
        :param log_level: logging level
        """
        self.__logger.setLevel(log_level)

    def get_logger(self):
        """
        :return:return logger class instance
        """
        return self.__logger
