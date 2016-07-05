__author__ = 'izrik'

import os.path
import urllib2

pypi = 'https://pypi.python.org/pypi'

class StoreRoom(object):
    path = ''

    def __init__(self):
        self.path = os.path.expanduser("~/.householder")

    def import_module(self, module_name, version=None):
        if not is_module_cached(module_name, version):
            cache_module(module_name, version)
        pass

    def is_module_cached(self, module_name, version):
        exact_path = os.path.join(self.path, module_name, version)
        return os.path.exists(exact_path) and os.path.isdir(exact_path)

    def cache_module(self, module_name, version):
        urllib2.Request(pypi)
http://pypi.python.org/pypi/<package_name>/json
        pass


default_instance = StoreRoom()

import_module = default_instance.import_module
