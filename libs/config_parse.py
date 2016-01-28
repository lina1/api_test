__author__ = 'lina'

import ConfigParser


class Config:

    def __init__(self, path="../config/yaml_config.ini"):
        self.path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)

    def get(self, field, key):
        result = ""
        try:
            result = self.cf.get(field, key)
        except Exception, e:
            result = ""
        return result

    def set(self, field, key, value):
        try:
            self.cf.set(field, key, value)
            self.cf.write(open(self.path, 'w'))
        except:
            return False
        return True

