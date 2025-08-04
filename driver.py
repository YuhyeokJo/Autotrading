from abc import ABC, abstractmethod

from kiwer_api import KiwerAPI
from nemo_api import NemoAPI


class StockBrokerDriverInterface(ABC):
    @abstractmethod
    def login(self, user_id: str, password: str) -> bool:
        pass

    @abstractmethod
    def get_price(self, symbol: str) -> float:
        pass

    @abstractmethod
    def buy(self, symbol: str, quantity: int) -> bool:
        pass

    @abstractmethod
    def sell(self, symbol: str, price: int, quantity: int) -> bool:
        pass


class MockDriver(StockBrokerDriverInterface):
    def __init__(self):
        self.logged_in = False

    def login(self, user_id: str, password: str) -> bool:
        self.logged_in = True
        return True

    def sell(self, symbol: str, price: int, quantity: int) -> bool:
        return True


class NemoDriver(StockBrokerDriverInterface):

    def login(self, user_id: str, password: str) -> bool:
        pass

    def get_price(self, symbol: str) -> float:
        pass

    def buy(self, symbol: str, quantity: int) -> bool:
        pass

    def __init__(self):
        self.api = NemoAPI()

    def sell(self, symbol: str, price: int, quantity: int) -> bool:
        self.api.selling_stock(symbol, price, quantity)
        return True


class KiwerDriver(StockBrokerDriverInterface):
    def __init__(self):
        self.api = KiwerAPI()

    def login(self, user_id: str, password: str) -> bool:
        pass

    def get_price(self, symbol: str) -> float:
        pass

    def buy(self, symbol: str, quantity: int) -> bool:
        pass

    def sell(self, symbol: str, price: int, quantity: int) -> bool:
        self.api.sell(symbol, quantity, price)
        return True

