import random
import math

from src.selection.Selection import Selection

class Boltzmann(Selection):
    tc = 0
    t0 = 0
    k = 0
    generation = 0

    def set_temperature(self, tc: int, t0: int, k: int, generation: int):
        self.tc = tc
        self.t0 = t0
        self.k = k
        self.generation = generation

    def select(self, population: [], individuals: int):
        temperature = self.TC + (self.T0 + self.TC) * math.exp(-self.K * self.generation)
