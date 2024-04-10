from src.cutoff.Cutoff import Cutoff
import math

GEN_MAX = 5

class Structure(Cutoff):

    @staticmethod
    def should_cutoff(current_population, old_population, generation, cutoff_value):
        if(generation == 0):
            return False
        mutual_elements = current_population
        times = len(old_population)
        gen_index = max(0, times - GEN_MAX)
        for i in range(gen_index, times):
            mutual_elements = [x for x in mutual_elements if x in old_population[i]]
            if len(mutual_elements)/len(current_population) < cutoff_value:
                return False
        return True
