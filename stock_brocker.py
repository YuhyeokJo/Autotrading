from driver import MockDriver, KiwerDriver, NemoDriver


class StockBrocker:  #<----Driver Interface????
    def __init__(self, name):
        if name == "mock":
            self._driver = MockDriver()
        elif name == "kiwer":
            self._driver = KiwerDriver()
        elif name == "nemo":
            self._driver = NemoDriver()
        else:
            raise NotImplementedError

    def login(self, id, password):
        self._driver.login(id, password)

    def buy(self, 종목코드, 가격, 수량):
        pass

    def sell(self, 종목코드, 가격, 수량):
        pass

    def get_price(self, 종목코드):
        pass

    def buy_nice_timing(self, 종목, 금액):
        """
        ▪ 기능1 : buyNiceTiming(종목, 금액)
        • 200ms 주기로 3회 가격을 읽고, 가격이 올라가는추세인지파악한다.
        • 가격이 올라가는 추세라면, 총 금액을 최대한 사용하여최대수량만큼매수한다.
        • 마지막에읽은가격으로매수한다.
        """
        pass

    def sell_nice_timing(self, 종목, 수량):
        """
        ▪ 기능2 : sellNiceTiming(종목, 수량)
        • 200ms 주기로 3회 가격을 읽고, 가격이 내려가는 추세인지 파악한다.
        • 가격이내려가는추세라면, 사용자가설정한수량만큼주식을모두매도한다.
        • 마지막에읽은가격으로매도한다.
        """
        pass
