from src.operators.crossing.Crossing import Crossing
import random
from src.classes.attributes.AttributeSet import AttributeSet
class OnePoint(Crossing):

    def cross(parent1, parent2):
        parent1_arr = parent1.to_array()
        parent2_arr = parent2.to_array()
        point = random.randrange(1, len(parent1_arr))
        child1 = parent1_arr[:point] + parent2_arr[point:]
        child2 = parent2_arr[:point] + parent1_arr[point:]
        return AttributeSet.from_array(child1), AttributeSet.from_array(child2)