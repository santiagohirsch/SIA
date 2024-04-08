from selection.Selection import Selection
import random

class Roulette(Selection):
    def select(population, individuals):
        total_fitness = sum(individual.fitness() for individual in population)
        selection_probs = [individual.fitness() / total_fitness for individual in population]

        selected = []

        for _ in range(individuals):
            pick = random.random()
            current = 0
            for i in range(len(population)):
                current += selection_probs[i]
                if current > pick:
                    selected.append(population[i])
                    break
        return selected
    