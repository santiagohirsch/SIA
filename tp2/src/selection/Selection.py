from abc import ABC, abstractmethod

class Selection(ABC):
    @abstractmethod
    def select(population, individuals):
        pass