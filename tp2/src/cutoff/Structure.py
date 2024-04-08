from src.cutoff.Cutoff import Cutoff
import math

GEN_MAX = 5

class Structure(Cutoff):

    @staticmethod
    def should_cutoff(current_population, old_population, generation, cutoff_value):
        mutual_elements = current_population
        times = len(old_population)
        for i in range(times - GEN_MAX, times):
            mutual_elements = list.filter(lambda x: x in mutual_elements, old_population[i])
            if len(mutual_elements)/len(current_population) < cutoff_value:
                return False
        return True
