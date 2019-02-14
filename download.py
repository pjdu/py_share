from down.stocks import stocks
class down:
    def __init__(self):
        pass
    def download(self):
        sinfo = stocks()
        sinfo.update_stock_basic()
        codes = sinfo.get_codes()
        #for code in codes:
        #    print(code)

if __name__ == "__main__":
    d = down()
    d.download()