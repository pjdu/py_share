from config import *
from util.dir_util import dir_util

class data_file(dir_util):
    def __init__(self, date, name):
        dir_util.__init__(self, os.path.join(namespace.ROOT, date))
        self._date = date
        self._daily_path = os.path.join(os.path.join(namespace.ROOT, self._date), name)
    def have_daily_data(self):
        return os.path.exists(self._daily_path)