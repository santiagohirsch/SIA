from src.selection.Selection import Selection
import random
import numpy as np
import math


class DeterministicTournament(Selection):    

    k = 10

    @classmethod
    def define_params(self, k):
        self.k = k

    @classmethod
    def select(self, population, individuals):
        selected = []
        for i in range(individuals):
            selected.append(DeterministicTournament.tournament(self,population))
        return selected
    

    def tournament(self,population):
        print("k",self.k)
        selected = []
        for _ in range(self.k):
            selected.append(random.choice(population))
        best = selected[0]
        for i in range(1, self.k):
            if selected[i].fitness() > best.fitness():
                best = selected[i]
        return best