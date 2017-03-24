__author__ = 'muralidharan'

class Constants(object):
    dummy = "dummy"
    TIME_FORMAT = '%Y%m%d_%H%M%S%f'
    LOG_FILE_PATH = "../log_files/"
    LOG_EXT = '.log'

    ################# CUSTOM EXCEPTION##################

    PY_INITIALIZE_FAILURE = ('PY_INITIALIZE_FAILURE', "Initialization failed in host {0},{1}")
    PY_MODULE_ONE_FAILURE = ('PY_MODULE_ONE_FAILURE', "Module one failure in host {0},{1}")
