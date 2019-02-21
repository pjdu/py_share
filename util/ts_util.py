from comm_pkg import *
from util.pd_list_util import *
class ts_util(pd_list_util):
    def __init__(self):
        pd_list_util.__init__(self)
        self._pro = ts.pro_api("3b239c5c08e5e691a718fb15dd986555fe2f7b11f1b078af61692fe0")
        pass
    def is_trade_date(self, start_date, end_data):
        pd = self._pro.trade_cal(exchange='', start_date=start_date, end_date=end_data)
        values = self._pd_2_int64(pd['is_open'])
        return values
    def get_trade_daily(self, date):
        pd = self._pro.daily(trade_date=date)
        return pd
    