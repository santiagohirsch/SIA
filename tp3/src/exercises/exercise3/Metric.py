from abc import ABC, abstractmethod

class Metric(ABC):
    @classmethod
    @abstractmethod
    def calculate(self, true_positive, true_negative, false_positive, false_negative):
        pass