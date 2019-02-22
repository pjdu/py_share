from config import *

class list_util:
    def __init__(self):
        pass
    @abstractmethod
    def _cmp(self, arg1, arg2):
        #print(arg1.cmp(arg1, arg2))
        if(len(arg1) != len(arg2)):
            return False
        else:
            for a1 in arg1:
                if (a1 not in arg2) :
                    return False
        return True