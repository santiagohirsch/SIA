from abc import ABC, abstractmethod

class Attribute(ABC):
    def __init__(self, value: float):
        self.value = value

    @abstractmethod
    def __str__(self):
        self.value.__str__()

    