from abc import ABC, abstractmethod

class Attribute(ABC):
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return self.value.__str__()
    


    