from abc import ABC, abstractmethod

class Cutoff(ABC):
    @classmethod
    @abstractmethod
    def should_cutoff(self, current_population, old_population, generation, cutoff_value):
        pass