__author__ = 'lina'

import logging
import time
from robot.api import logger
from logging.handlers import TimedRotatingFileHandler


class _logging():

    def __init__(self):

        logging.basicConfig(
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='../logs/api_test_%s.log' % time.strftime("%Y-%m-%d", time.localtime()),
                    filemode='a')

        # self.nor = logging.getLogger("nor")
        # self.nor.setLevel(logging.INFO)
        # fileHandler = TimedRotatingFileHandler('../logs/api_test', when='midnight')
        # fileHandler.suffix = '%Y%m%d.log'
        # self.nor.addHandler(fileHandler)

        # logHandler = TimedRotatingFileHandler('../logs/api_test.log', when='midnight')
        # logFormatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
        # logHandler.setFormatter(logFormatter)
        # self.logger = logging.getLogger("MyLogger")
        # self.logger.addHandler(logHandler)
        # self.logger.setLevel(logging.INFO)

    def _debug(self, message):

        # logger.debug(msg=message)
        logging.debug(msg=message)

    def _info(self, message):

        # logger.info(msg=message)
        logging.info(msg=message)
        # self.logger.info(msg=message)

    def _error(self, message):

        logging.error(msg=message)

    def _console(self, message):

        logger.console(msg=message)

    def _exception(self, message):

        logging.exception(msg=message)

    def _trace(self, message):

        logger.trace(msg=message)

    def _warn(self, message):

        # logger.warn(msg=message)
        logging.warning(msg=message)