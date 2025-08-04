from abc import ABC, abstractmethod


class StockBrokerDriverInterface(ABC):
    @abstractmethod
    def login(self, user_id: str, password: str) -> bool:
        pass

    @abstractmethod
    def get_price(self, symbol: str) -> float:
        pass

    @abstractmethod
    def buy(self, stock_code: str, price: float, counts: int):
        pass

    @abstractmethod
    def sell(self, symbol: str, quantity: int) -> bool:
        pass


class MockDriver(StockBrokerDriverInterface):
    def __init__(self):
        self.logged_in = False

    def login(self, user_id: str, password: str) -> bool:
        self.logged_in = True
        return True

    def buy(self, stock_code: str, price: float, counts: int):
        return f"[mock] {stock_code}, {price}, {counts} buy success"

    def get_price(self, symbol: str) -> float:
        pass

    def sell(self, symbol: str, quantity: int) -> bool:
        pass

class NemoDriver:
    pass


class KiwerDriver:
    pass