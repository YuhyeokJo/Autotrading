from driver import MockDriver, StockBrokerDriverInterface, NemoDriver, KiwerDriver


class AutoTradingSystem:
    def __init__(self, api_name: str, driver: StockBrokerDriverInterface):
        self.api_name = api_name
        self.driver = self._resolve_driver(driver, api_name)
        self.logged_in = False

    def _resolve_driver(self, driver, api_name: str) -> StockBrokerDriverInterface:

        if driver is StockBrokerDriverInterface:
            return self._get_driver(api_name)

        if isinstance(driver, type) and issubclass(driver, StockBrokerDriverInterface):
            return self._get_driver(api_name)

        return driver

    @staticmethod
    def _get_driver(api_name: str) -> StockBrokerDriverInterface:
        if api_name == "mock":
            return MockDriver()
        elif api_name == "nemo":
            return NemoDriver()
        elif api_name == "kiwer":
            return KiwerDriver()
        else:
            raise ValueError(f"Unsupported API: {api_name}")

    @classmethod
    def select_stock_brocker(cls, api_name: str) -> "AutoTradingSystem":
        driver = cls._get_driver(api_name)
        return cls(api_name, driver)

    def login(self, user_id: str, password: str) -> str:
        if self.driver.login(user_id, password):
            self.logged_in = True
            return f"[{self.api_name}] {user_id} login success"
        else:
            return f"[{self.api_name}] {user_id} login failed"