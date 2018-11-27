from comm_pkg import *
from util.util import util

STOCK_BASICS_NAME = "data\\stock_basics.csv"
INDEX_COL_NAME = "ts_code"

class stock_info(util):
    def __init__(self):
        util.__init__(self)
        self.__code = None
    def _check_code(self, pd1, pd2):
        code1 = self._ts_code_2_list(pd1.index)
        code2 = self._ts_code_2_list(pd2.index)
        #self._dbg(pd2.index)
        return self._cmp(code1, code2)
    def update_stock_basic(self, force = 0):
        df_new = self._pro.stock_basic()
        df_new = df_new.set_index(INDEX_COL_NAME, drop=True)
        #print(df_new)
        #df_new = df_new[[INDEX_COL_NAME,]]
        #print(df_new)
        self._dbg("dbg test\n")
        #asdfssdf
        if(force):
            self._dbg("force generate new\n")
            self.__code = self._ts_code_2_list(df_new.index)
            df_new.to_csv(STOCK_BASICS_NAME)
        else:
            df_old = None
            wrong_file = 0
            try:
                df_old = pd.read_csv(STOCK_BASICS_NAME, index_col = INDEX_COL_NAME)
            except Exception:
                wrong_file = 1
            if (1 == wrong_file):
                self._dbg("wrong file, generate new\n")
                df_new.to_csv(STOCK_BASICS_NAME)
            elif(False == self._check_code(df_new, df_old)):
                self._dbg("code dose not match, generate new\n")
                df_new.to_csv(STOCK_BASICS_NAME)
            self.__code = self._ts_code_2_list(df_new.index)
        return
    def get_code(self):
        return self.__code
