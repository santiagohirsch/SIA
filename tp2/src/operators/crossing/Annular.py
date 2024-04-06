from math import ceil
from src.operators.crossing.Crossing import Crossing
import random
from src.classes.attributes.AttributeSet import AttributeSet

class Annular(Crossing):

    def cross(parent1, parent2):
        parent1_arr = parent1.to_array()
        parent2_arr = parent2.to_array()
        parent_len = len(parent1_arr)
        point = random.randrange(1, parent_len)
        length = random.randrange(1, ceil(parent_len/2))
        child1 = parent1_arr.copy()
        child2 = parent2_arr.copy()
        for i in range(length):
            child1[(point+i) % parent_len] = parent2_arr[(point+i) % parent_len]
            child2[(point+i) % parent_len] = parent1_arr[(point+i) % parent_len]

        return AttributeSet.from_array(child1), AttributeSet.from_array(child2)
    