from src.selection.Selection import Selection

class Elite(Selection):
    
    @classmethod
    def select(self, population, individuals):
        new_population = []
        sorted_population = sorted(population, reverse=True, key=lambda individual: individual.fitness())
        i = 0
        k = 0
        while i < individuals:
            new_population.append(sorted_population[k])
            k += 1
            i += 1
            if k == len(sorted_population):
                k = 0
        return new_population