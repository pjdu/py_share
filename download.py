from down.stock_info import stock_info
class down:
    def __init__(self):
        pass
    def download(self):
        sinfo = stock_info()
        sinfo.update_stock_basic()
        codes = sinfo.get_code()
        for code in codes:
            print(code)

if __name__ == "__main__":
    d = down()
    d.download()