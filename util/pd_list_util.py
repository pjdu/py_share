from config import *

class pd_list_util:
    def __init__(self):
        pass
    def _pd_2_int64(self, pd):
        return pd.astype("int64").values.tolist()
    def _pd_2_object(self, pd):
        return pd.astype("object").values.tolist()
    def _ts_code_2_list(self, pd):
        return self._pd_2_object(pd)