from src.cutoff.Cutoff import Cutoff

class MaxGenerations(Cutoff):
    @classmethod
    def should_cutoff(self, current_population, old_population, generation, cutoff_value):
        return generation >= cutoff_value