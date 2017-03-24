__author__ = 'muralidharan'


class PYExceptions(Exception):
    """
    Son BR Exception class which takes tuple as argument and
    frame the error message for the given exception
    SON_BR_AUTHENTICATION_FAILURE , SON_BR_CONN_FAILURE , SON_BR_BACKUP_COLL_FAILURE so on.
    Define the custom exception and pass exception name and message here.
    """
    def __init__(self, *args, **kwargs):
        super(PYExceptions, self).__init__(self, *args, **kwargs)
        self.message = 'Error: {0} {1}'.format(args[0][0], args[0][1].format(args[1], args[2]))

    def __str__(self):
        """
        Custom SON BR Exception str msg
        :return: repr of message
        """
        return repr(self.message)
