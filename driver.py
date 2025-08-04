from abc import ABC, abstractmethod

from kiwer_api import KiwerAPI
from nemo_api import NemoAPI


class Driver(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def sell(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class MockDriver(Driver):
    pass


class KiwerDriver(Driver):
    def __init__(self):
        self.api = KiwerAPI()

    def login(self):
        pass

    def buy(self):
        pass

    def sell(self):
        pass

    def get_price(self):
        pass


class NemoDriver(Driver):
    def __init__(self):
        self.api = NemoAPI()

    def login(self):
        pass

    def buy(self):
        pass

    def sell(self):
        pass

    def get_price(self):
        pass
