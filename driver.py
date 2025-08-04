from abc import ABC, abstractmethod


class Driver(ABC):
    @abstractmethod
    def login(self, id: str, password: str):...