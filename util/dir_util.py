from config import *
class dir_util:
    def __init__(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)