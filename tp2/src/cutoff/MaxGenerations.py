from src.cutoff.Cutoff import Cutoff

class MaxGenerations(Cutoff):
    @staticmethod
    def should_cutoff(current_population, old_population, generation, cutoff_value):
        return generation >= cutoff_value