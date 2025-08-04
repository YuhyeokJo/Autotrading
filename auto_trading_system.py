import time
from driver import MockDriver, StockBrokerDriverInterface


class AutoTradingSystem:
    def __init__(self, api_name: str, driver: StockBrokerDriverInterface):
        self.api_name = api_name
        self._driver = driver
        self.logged_in = False

    @classmethod
    def select_stock_brocker(cls, api_name: str) -> "AutoTradingSystem":
        if api_name == "mock":
            driver = MockDriver()
        else:
            raise ValueError(f"Unsupported API: {api_name}")

        return cls(api_name, driver)

    def login(self, user_id: str, password: str) -> str:
        if self._driver.login(user_id, password):
            self.logged_in = True
            return f"[{self.api_name}] {user_id} login success"
        else:
            return f"[{self.api_name}] {user_id} login failed"

    def buy(self, stock_code: str, price: int, counts: int):
        return self._driver.buy(stock_code, price, counts)

    def buy_nice_timing(self, stock_code, total_price):
        time_interval = 0.2
        cnt = 0

        time.sleep(time_interval)
        highest_price = self._driver.get_price(stock_code)

        time.sleep(time_interval)
        cur_price = self._driver.get_price(stock_code)
        if highest_price < cur_price:
            highest_price = cur_price
            cnt += 1

        time.sleep(time_interval)
        cur_price = self._driver.get_price(stock_code)
        if highest_price < cur_price:
            highest_price = cur_price
            cnt += 1

        if cnt >= 2:
            counts = total_price / highest_price
            print("DEBUG3")
            return self._driver.buy(stock_code, highest_price, counts)

    def sell_nice_timing(self, stock_code, counts):
        pass
