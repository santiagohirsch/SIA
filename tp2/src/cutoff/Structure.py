from src.cutoff.Cutoff import Cutoff
import math

GEN_MAX = 5

class Structure(Cutoff):

    max_generations = GEN_MAX

    @classmethod
    def set_max_generations(self, max_generations):
        self.max_generations = max_generations 

    @classmethod
    def should_cutoff(self, current_population, old_population, generation, cutoff_value):
        if(generation == 0):
            return False
        mutual_elements = current_population
        times = len(old_population)
        gen_index = max(0, times - self.max_generations)
        for i in range(gen_index, times):
            mutual_elements = [x for x in mutual_elements if x in old_population[i]]
            if len(mutual_elements)/len(current_population) < cutoff_value:
                return False
        return True
