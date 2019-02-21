from comm_pkg import *
from comm_pkg import namespace as ns
from util.util import util
from util.dir_util import dir_util
from util.ts_util import ts_util


class stocks(util, dir_util, ts_util):
    def __init__(self):
        dir_util.__init__(self, ns.root)
        util.__init__(self)
        ts_util.__init__(self)
        self.__codes = None
        self.__sinfo_path = os.path.join(ns.root, ns.sinfo_name)
    def _cmp_codes(self, pd1, pd2):
        code1 = self._ts_code_2_list(pd1.index)
        code2 = self._ts_code_2_list(pd2.index)
        #self._dbg(pd2.index)
        return self._cmp(code1, code2)
    def update_stock_basic(self, force = 0):
        df_new = self._pro.stock_basic()
        df_new = df_new.set_index(ns.sinfo_idx, drop=True)
        #print(df_new)
        #df_new = df_new[[INDEX_COL_NAME,]]
        #print(df_new)
        self.dbg("dbg test\n")
        #asdfssdf
        if(force):
            self.info("force generate new\n")
            self.__codes = self._ts_code_2_list(df_new.index)
            df_new.to_csv(self.__sinfo_path)
        else:
            df_old = None
            wrong_file = 0
            try:
                df_old = pd.read_csv(self.__sinfo_path, index_col = ns.sinfo_idx)
            except Exception:
                wrong_file = 1
            if (1 == wrong_file):
                self.info("wrong file, generate new\n")
                df_new.to_csv(self.__sinfo_path)
            elif(False == self._cmp_codes(df_new, df_old)):
                self.info("code dose not match, generate new\n")
                df_new.to_csv(self.__sinfo_path)
            self.__codes = self._ts_code_2_list(df_new.index)
        return
    def get_codes(self):
        return self.__codes
