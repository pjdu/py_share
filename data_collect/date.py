from comm_pkg import *
from util.util import util
from util.dir_util import dir_util

class date(util, dir_util):
    def __init__(self, date):
        util.__init__(self)
        dir_util.__init__(self, os.path.join(namespace.ROOT, date))
        self.__date = date
        self.__daily_path = os.path.join(os.path.join(namespace.ROOT, self.__date), 'daily.csv')
    def write_daily(self, pd):
        pd.to_csv(self.__daily_path)
    def have_daily_data(self):
        return os.path.exists(self.__daily_path)