from abc import ABC, abstractmethod

class Selection(ABC):
    @classmethod
    @abstractmethod
    def select(self, population, individuals):
        pass