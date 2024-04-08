from abc import ABC, abstractmethod

class Replacement(ABC):
    @abstractmethod
    def replace(population, children, population_individuals, children_individuals, B):
        pass