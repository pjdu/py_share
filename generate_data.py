#from data_collect.stocks import stocks
from util.ts_util import *
from util.debug_util import *
from data_collect.date import *
from config import *
import time
class gen():
    def __init__(self):
        self._share = ts_util()
        pass
    def list_trade_date(self):
        iter_time = time.mktime((namespace.YEAR, namespace.MONTH, namespace.DAY, 9, 44, 31, 6, 273, 0))
        begin = time.strftime("%Y%m%d", time.localtime(iter_time))
        end = time.strftime("%Y%m%d", time.localtime())
        values = self._share.is_trade_date(begin, end)
        for v in values:
            now = time.strftime("%Y%m%d", time.localtime(iter_time))
            print("date:", now, "trade:",v)
            if v == 1:
                obj_date = date(now)
                if False == obj_date.have_daily_data() or namespace.FORCE_WRITE == True:
                    obj_date.write_daily(self._share)
            iter_time = iter_time + 24*60*60
        pass

if __name__ == "__main__":
    obj_gen = gen()
    obj_gen.list_trade_date()
    
    