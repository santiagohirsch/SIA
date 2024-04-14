import random
import math

from src.selection.Selection import Selection

class Boltzmann(Selection):

    def __init__(self, tc: int, t0: int, k: int, generation: int):
        self.tc = tc
        self.t0 = t0
        self.k = k
        self.generation = generation

    def set_generation(self, generation):
        self.generation = generation

    def select(self, population, individuals):
        temperature = self.tc + (self.t0 + self.tc) * math.exp(-self.k * self.generation)
        selected = []
        fitness = [math.exp(individual.fitness()/temperature) for individual in population]
        average_fitness = sum(fitness) / len(fitness)
        values = [f/average_fitness for f in fitness]
        population_copy = [individual for individual in population]

        for _ in range(individuals):
            if len(population_copy) == 0:
                population_copy = [individual for individual in population]
                values = [f/average_fitness for f in fitness]
            individual = random.choices(population_copy, weights=values, k=1)[0]
            index = population_copy.index(individual)
            population_copy.pop(index)
            values.pop(index)
            selected.append(individual)
        self.generation += 1
        return selected


            
