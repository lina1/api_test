__author__ = 'lina'

from exceptions import Exception
from robot.errors import RobotError

class UrlError(RobotError):

    def __init__(self, value):

        self.value = value

    def __repr__(self):

        return repr(self.value)
