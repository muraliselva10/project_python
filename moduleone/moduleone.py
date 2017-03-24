__author__ = 'muralidharan'

from project_python.commonutils.Logger import Logger
from project_python.commonutils.PYExceptions import PYExceptions
from project_python.commonutils.Constants import Constants as const

logger = Logger().get_logger()

class ModuleOne(object):

    def __init__(self):

        self.variable = "module_one"
        self.host = "10.61.9.151"

    def module_one_main(self):

        try:
            new_variable = self.variable
            logger.debug("Inside the module one main function in host {0}".format(self.host))
        except PYExceptions as e:
            raise PYExceptions(const.PY_MODULE_ONE_FAILURE, self.host, e)
