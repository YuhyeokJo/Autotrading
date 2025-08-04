from abc import ABC, abstractmethod


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


class NemoDriver:
    pass


class KiwerDriver:
    pass