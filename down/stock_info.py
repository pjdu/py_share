from comm_pkg import *
from comm_pkg import namespace as ns
from util.util import util


class stock_info(util):
    def __init__(self):
        util.__init__(self, ns.root)
        self.__code = None
        self.__sinfo_path = os.path.join(ns.root, ns.sinfo_name)
    def _check_code(self, pd1, pd2):
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
        self._dbg("dbg test\n")
        #asdfssdf
        if(force):
            self._dbg("force generate new\n")
            self.__code = self._ts_code_2_list(df_new.index)
            df_new.to_csv(self.__sinfo_path)
        else:
            df_old = None
            wrong_file = 0
            try:
                df_old = pd.read_csv(self.__sinfo_path, index_col = ns.sinfo_idx)
            except Exception:
                wrong_file = 1
            if (1 == wrong_file):
                self._dbg("wrong file, generate new\n")
                df_new.to_csv(self.__sinfo_path)
            elif(False == self._check_code(df_new, df_old)):
                self._dbg("code dose not match, generate new\n")
                df_new.to_csv(self.__sinfo_path)
            self.__code = self._ts_code_2_list(df_new.index)
        return
    def get_code(self):
        return self.__code
