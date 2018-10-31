import tushare as ts
import pandas as pd

STOCK_BASICS_NAME = "data\\stock_basics.csv"
INDEX_COL_NAME = "code"

class Stock:
    def __init__(self):
        __code = None
    def check_code(self, pd1, pd2):
        code1 = pd1.index.values
        code2 = pd2.index.values
        if(len(code1) != len(code2)):
            print("code len does not match")
            return 1
        for(c1, c2) in zip(code1, code2):
            if int(c1) != int(c2):
                print("code %d != %d" % (c1, c2))
                return 1
        return 0
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
if __name__ == "__main__":
    stock = Stock()
    stock.update_stock_basic()