from config import *

class debug_util:
    def __init__(self):
        self.__dbg = namespace.DEBUG
        self.__info = namespace.INFO
        self.__warn = namespace.WARN
        self.__err = namespace.ERR
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