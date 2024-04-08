from abc import ABC, abstractmethod

class Cutoff(ABC):
    @abstractmethod
    def should_cutoff(current_population, old_population, generation, cutoff_value):
        pass