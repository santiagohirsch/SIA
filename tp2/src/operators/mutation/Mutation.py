from abc import ABC, abstractmethod
from src.classes.attributes.AttributeSet import AttributeSet

class Mutation(ABC):
    @abstractmethod
    def mutate(parent: AttributeSet, mutation_rate: float):
        pass