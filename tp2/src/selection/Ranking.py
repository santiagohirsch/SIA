from src.selection.Selection import Selection
import random

class Ranking(Selection):
    
    @staticmethod
    def select(population, individuals):
        sorted_population = sorted(population, key=lambda x: x.fitness(), reverse=True)
        function_population = []
        length = len(sorted_population)

        for i in enumerate(sorted_population):
            function_population.append((length-i+1)/length)

        selected = []

        for _ in range(individuals):
            pick = random.random()
            current = 0
            for i in range(len(population)):
                current += function_population[i]
                if current > pick:
                    selected.append(population[i])
                    break

        return selected