from comm_pkg import *
from util.util import util

STOCK_BASICS_NAME = "data\\stock_basics.csv"
INDEX_COL_NAME = "code"

class stock_info(util):
    def __init__(self):
        __code = None
    def check_code(self, pd1, pd2):
        code1 = list(pd1.index.values)
        code2 = list(pd2.index.values)
        return self.cmp(code1, code2)
    def update_stock_basic(self, force = 0):
        df_new = ts.get_stock_basics()
        if(force):
            print("force generate new\n")
            __code = df_new.index.values
            df_new.to_csv(STOCK_BASICS_NAME)
            return
        df_old = None
        no_file = 0
        try:
            df_old = pd.read_csv(STOCK_BASICS_NAME, index_col = INDEX_COL_NAME)
        except Exception:
            no_file = 1
        if (1 == no_file):
            print("no file, generate new\n")
            df_new.to_csv(STOCK_BASICS_NAME)
        elif(self.check_code(df_new, df_old)):
            print("code dose not match, generate new\n")
            df_new.to_csv(STOCK_BASICS_NAME)
        __code = df_new.index.values
        return
