from config import *
from util.util import util
import data_file

class stock(util, data_file):
    def __init__(self, code, date):
        util.__init__(self)
        data_file.__init__(self, date, code + '.daily.csv')
        self.__code = code
    def write_code_daily(self, share):
        pd = share.get_trade_daily(self._date)
        pd.to_csv(self._daily_path)