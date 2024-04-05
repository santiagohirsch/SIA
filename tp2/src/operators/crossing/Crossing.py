from abc import ABC, abstractmethod
from src.classes.attributes.AttributeSet import AttributeSet

class Crossing(ABC):
    @abstractmethod
    def cross(parent1: AttributeSet, parent2: AttributeSet):
        pass