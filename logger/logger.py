import logging


class Logger(object):
    LOGGER_FORMAT = u'%(filename)s:%(lineno)d %(name)s %(levelname)s %(asctime)s  %(message)s'
    LOGGER_LEVEL = 'INFO'
    logging.basicConfig(level=LOGGER_LEVEL, format=LOGGER_FORMAT)

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
