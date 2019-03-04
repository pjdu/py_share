from config import *
from util.util import util
from data_collect.data_file import data_file

class stock(util, data_file):
    def __init__(self, code, date):
        util.__init__(self)
        data_file.__init__(self, date, code + '.daily.csv')
        self.__code = code
    def __write_stock_daily_old(self, share):
        code = self.__code.split('.')
        df = share.get_stock_daily(code[0], self._date)
        if(df != None):
            self.dbg('Write code = ' + code[0] + 'date = ' + self._date + '\n')
            df.to_csv(self._daily_path)
            return 1
        else:
            self.dbg('Not exits code = ' + code[0] + 'date = ' + self._date + '\n')
            self.write_empty_file()
            return 0
        #adsfdsfas
        #pd.to_csv(self._daily_path)
    def write_stock_daily(self, share):
        return self.__write_stock_daily_old(share)