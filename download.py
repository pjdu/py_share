from down.stock_info import stock_info
class down:
    def __init__(self):
        self.stock = stock_info()
    def download(self):
        self.stock.update_stock_basic()
        code = self.stock.get_code()
if __name__ == "__main__":
    d = down()
    d.download()