from src.selection.Selection import Selection
import random
import numpy as np
import math

class ProbabilisticTournament(Selection):
    
    @classmethod
    def select(self, population, individuals):
        selected = []
        for i in range(individuals):
            selected.append(ProbabilisticTournament.tournament(population))
        return selected
    
    @staticmethod
    def tournament(population):
        k = 2
        selected = []
        threshold = random(0.5,1)
        for _ in range(k):
            selected.append(random.choice(population))
        best = selected[0]
        for i in range(1, k):
            r = random.uniform(0,1)
            if selected[i].fitness() > best.fitness():
                if(r < threshold):
                    best = selected[i]
            else:
                if(r > threshold):
                    best = selected[i]
        return best