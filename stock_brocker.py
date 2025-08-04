from driver import Driver

class StockBrocker:
    def __init__(self, name: str, driver: Driver):
        self._name = name
        self._driver = driver

    def login(self, id: str, password: str):
        return self._driver.login(id, password)