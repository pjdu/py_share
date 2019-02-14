import tushare as ts
import pandas as pd
from abc import ABCMeta, abstractmethod
import os
class namespace:
    root = "data"
    sinfo_name = "stock_basics.csv"
    sinfo_idx = "ts_code"
    debug = 0
    warn = 1
    err = 1
    info = 1

