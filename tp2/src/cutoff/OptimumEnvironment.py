from src.cutoff.Cutoff import Cutoff

class OptimumEnvironment(Cutoff):
    @classmethod
    def should_cutoff(self, current_population, old_population, generation, cutoff_value):
        return max([individual.fitness() for individual in current_population]) >= cutoff_value