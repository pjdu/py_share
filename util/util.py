from comm_pkg import *

class util:
    def __init__(self):
        pass
    @abstractmethod
    def cmp(self, arg1, arg2):
        if(len(arg1) != len(arg2)):
            return False
        else:
            for a1 in arg1:
                if a1 not in arg2:
                    return False
        return True