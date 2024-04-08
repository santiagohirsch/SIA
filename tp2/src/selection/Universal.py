from src.selection.Selection import Selection
import random

class Universal(Selection):
    def select(population, individuals):
        total_fitness = sum(individual.fitness() for individual in population)
        selection_probs = [individual.fitness() / total_fitness for individual in population]

        selected = []
        r = random.uniform(0, 1)
        for index in range(individuals):
            current = 0
            value = (r + index)/individuals
            for i in range(len(population)):
                current += selection_probs[i]
                if current > value:
                    selected.append(population[i])
                    break
        return selected
        

