# -*- coding:utf-8 -*-

from distutils.version import LooseVersion
from . import sussexkeyboard

try:
    import galicaster
except:
    print "Error: Galicaster not found"

def init():
    if LooseVersion(galicaster.__version__) <= LooseVersion("2.1.x"):
        sussexkeyboard.init()
    else:
        raise Exception("Plugin version mismatch")
