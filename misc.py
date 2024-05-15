import os
import traceback

class UserConfig:

    def __init__(self):
        self.user_namespace = {}

    def reload(self, filename):
        fd = open(filename, 'rb')
        fileimage = fd.read()
        self.user_namespace = {}
        code = compile(fileimage, os.path.basename(filename), 'exec')
        exec(code, self.user_namespace, self.user_namespace)

    def get(self, symbol_name, default=None):
        try:
            return self.user_namespace[symbol_name]
        except KeyError:
            if default is None:
                raise
            return default
