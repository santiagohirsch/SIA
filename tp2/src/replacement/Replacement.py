from abc import ABC, abstractmethod

class Replacement(ABC):
    @abstractmethod
    def replace(population, children, selection1, selection2, B):
        pass