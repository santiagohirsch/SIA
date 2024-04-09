from src.selection.Selection import Selection
import random
import numpy as np
import math


class DeterministicTournament(Selection):    
    @classmethod
    def select(self, population, individuals):
        selected = []
        for i in range(individuals):
            selected.append(DeterministicTournament.tournament(population))
        return selected
    
    @staticmethod
    def tournament(population):
        selected = []
        k = 10
        for _ in range(k):
            selected.append(random.choice(population))
        best = selected[0]
        for i in range(1, k):
            if selected[i].fitness() > best.fitness():
                best = selected[i]
        return best