#from data_collect.stocks import stocks
from util.ts_util import *
from util.debug_util import *
from data_collect.date import *
from data_collect.stock import *
from config import *
import time
class gen():
    def __init__(self):
        self._share = ts_util()
        pass
    def add_day(self, time):
        return time + 24*60*60
    def write_stock(self, codes, date, share, force):
        count = len(codes)
        write = 0
        for code in codes:
            st = stock(code, date)
            if False == st.have_data() or force == True:
                    write = write + st.write_stock_daily(share)
        print("date = " + date + " have " + str(count) + " stocks" + " success write " + str(write))
    def list_trade_date(self):
        iter_time = time.mktime((namespace.YEAR, namespace.MONTH, namespace.DAY, 9, 44, 31, 6, 273, 0))
        begin = time.strftime("%Y%m%d", time.localtime(iter_time))
        end = time.strftime("%Y%m%d", time.localtime())
        values = self._share.is_trade_date(begin, end)
        for v in values:
            today = time.strftime("%Y%m%d", time.localtime(iter_time))
            print("date:", today, "trade:",v)
            if v == 1:
                obj_date = date(today)
                if False == obj_date.have_data() or namespace.FORCE_WRITE == True:
                    obj_date.write_daily(self._share)
                codes = obj_date.get_codes()
                self.write_stock(codes, today, self._share, namespace.FORCE_WRITE)
            iter_time = self.add_day(iter_time)
        pass

if __name__ == "__main__":
    obj_gen = gen()
    obj_gen.list_trade_date()