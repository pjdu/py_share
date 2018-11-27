from comm_pkg import *

class debug_util:
    def __init__(self, dbg=1, info=1, warn=1):
        self.__dbg = dbg
        self.__info = info
        self.__warn = warn
    def _dbg(self, arg1):
        if(self.__dbg):
            print(arg1, end='')
    def _info(self, arg1):
        if(self.__info):
            print(arg1, end='')
    def _warn(self, arg1):
        if(self.__warn):
            print(arg1, end='')