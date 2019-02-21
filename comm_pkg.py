import tushare as ts
import pandas as pd
from abc import ABCMeta, abstractmethod
import os
class namespace:
    ROOT = "data"
    SINFO_NAME = "stock_basics.csv"
    SINFO_IDX = "ts_code"
    DATE_BEGIN = '20140601'
    YEAR = 2014
    MONTH = 6
    DAY = 1
    DEBUG = 0
    WARN = 1
    ERR = 1
    INFO = 1
    FORCE_WRITE = False

