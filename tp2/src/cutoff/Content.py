from src.cutoff.Cutoff import Cutoff
import math

class Content(Cutoff):

    @staticmethod
    def should_cutoff(current_population, old_population, generation, cutoff_value):
        if generation < cutoff_value:
            return False
        new_gen_max = max([individual.fitness() for individual in current_population])
        for gen in range(generation - cutoff_value, generation):
            old_gen_max = max([individual.fitness() for individual in old_population[gen]])
            if not math.isclose(new_gen_max, old_gen_max, rel_tol=1e-6):
                return False
        return True
            