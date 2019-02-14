from comm_pkg import *

class debug_util:
    def __init__(self):
        self.__dbg = namespace.debug
        self.__info = namespace.info
        self.__warn = namespace.warn
        self.__err = namespace.err
    def dbg(self, arg1):
        if(self.__dbg):
            print(arg1, end='')
    def info(self, arg1):
        if(self.__info):
            print(arg1, end='')
    def warn(self, arg1):
        if(self.__warn):
            print(arg1, end='')
    def err(self, arg1):
        if(self.__err):
            print(arg1, end='')