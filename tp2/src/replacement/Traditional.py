from src.replacement.Replacement import Replacement
import math

class Traditional(Replacement):
    
    @staticmethod
    def replace(population, children, selection1, selection2, B):
        n = len(population)
        aux_population = population + children
        return selection1.select(aux_population, math.ceil(B * n)) + selection2.select(aux_population, math.floor((1 - B) * n))