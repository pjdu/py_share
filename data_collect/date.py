from config import *
from util.util import util
from data_collect.data_file import data_file

class date(util, data_file):
    def __init__(self, date):
        util.__init__(self)
        data_file.__init__(self, date, 'daily.csv')
    def write_daily(self, share):
        df = share.get_trade_daily(self._date)
        df.to_csv(self._daily_path)
    def get_codes(self):
        df_daily = pd.read_csv(self._daily_path)
        return self._ts_code_2_list(df_daily['ts_code'])