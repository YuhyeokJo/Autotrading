from driver import MockDriver, StockBrokerDriverInterface, NemoDriver, KiwerDriver


class AutoTradingSystem:
    def __init__(self, api_name: str, driver: StockBrokerDriverInterface):
        self.api_name = api_name
        self.driver = driver
        self.logged_in = False

    @classmethod
    def select_stock_brocker(cls, api_name: str) -> "AutoTradingSystem":
        if api_name == "mock":
            driver = MockDriver()
        elif api_name == 'nemo':
            driver = NemoDriver()
        elif api_name == 'kiwer':
            driver = KiwerDriver()
        else:
            raise ValueError(f"Unsupported API: {api_name}")

        return cls(api_name, driver)

    def login(self, user_id: str, password: str) -> str:
        if self.driver.login(user_id, password):
            self.logged_in = True
            return f"[{self.api_name}] {user_id} login success"
        else:
            return f"[{self.api_name}] {user_id} login failed"