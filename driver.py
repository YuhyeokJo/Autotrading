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
    def sell(self, symbol: str, quantity: int) -> bool:
        pass


class MockDriver(StockBrokerDriverInterface):
    def __init__(self):
        self.logged_in = False

    def login(self, user_id: str, password: str) -> bool:
        self.logged_in = True
        return True

    def get_price(self, symbol: str) -> float:
        pass

    def buy(self, symbol: str, quantity: int) -> bool:
        pass

    def sell(self, symbol: str, quantity: int) -> bool:
        pass



class NemoDriver(StockBrokerDriverInterface):
    def __init__(self):
        self.api = NemoAPI()
        self.logged_in = False

    def login(self, user_id: str, password: str) -> bool:
        try:
            self.api.cerification(user_id, password)
            self.logged_in = True
            return True
        except Exception as e:
            print(f"[NemoDriver] Login failed: {e}")


class KiwerDriver(StockBrokerDriverInterface):
    def __init__(self):
        self.api = KiwerAPI()
        self.logged_in = False

    def login(self, user_id: str, password: str) -> bool:
        try:
            self.api.login(user_id, password)
            self.logged_in = True
            return True
        except Exception as e:
            print(f"[NemoDriver] Login failed: {e}")

    def get_price(self, symbol: str) -> float:
        pass

    def buy(self, symbol: str, quantity: int) -> bool:
        pass

    def sell(self, symbol: str, quantity: int) -> bool:
        pass