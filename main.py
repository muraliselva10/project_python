__author__ = 'muralidharan'

import logging
import os, datetime, traceback
from project_python.commonutils.Logger import Logger
from project_python.commonutils.PYExceptions import PYExceptions
from project_python.commonutils.Constants import Constants as const
from project_python.moduleone.moduleone import ModuleOne

logger = Logger().get_logger()


class ProjectPython(object):

    def __init__(self):

        dummy_variable = const.dummy
        self.host = "10.61.9.151"

    def initialise_log(self):
        """
        Initialize log and set logging level .
        :return:
        """
        log_initialised = False
        try:
            log_path = const.LOG_FILE_PATH
            exec_time = datetime.datetime.now()
            log_folder = os.path.abspath(log_path)
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)
            log_file = os.path.join(os.path.abspath(log_folder),
                                'Log' + '_' + exec_time.strftime(const.TIME_FORMAT)[:-3] + const.LOG_EXT)
            print("Find the Log File Here : {0}".format(log_file))
            Logger().set_log_file(log_file)
            Logger().set_log_level(logging.DEBUG)
            log_initialised = True
        except Exception as e:
            print("Unable to Initialise log.")
            print(traceback.format_exc(e))
        return log_initialised, log_file

    def main(self):
        try:
            self.initialise_log()
            print("Process Initialized Succefully")
            logger.debug("Process Initialization in host {}".format(self.host))
            module_one = ModuleOne()
            module_one.module_one_main()
        except PYExceptions as e:
            raise PYExceptions(const.PY_INITIALIZE_FAILURE, self.host, e)
        except Exception as e:
            print("ERROR : {0}".format(e))
