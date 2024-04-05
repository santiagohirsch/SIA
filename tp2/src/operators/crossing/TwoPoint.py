from src.operators.crossing.Crossing import Crossing
import random
from src.classes.attributes.AttributeSet import AttributeSet

class TwoPoint(Crossing):

    def cross(parent1, parent2):
        parent1_arr = parent1.to_array()
        parent2_arr = parent2.to_array()
        point1 = random.randrange(1, len(parent1_arr))
        point2 = random.randrange(point1, len(parent1_arr))
        child1 = parent1_arr[:point1] + parent2_arr[point1:point2] + parent1_arr[point2:]
        child2 = parent2_arr[:point1] + parent1_arr[point1:point2] + parent2_arr[point2:]
        return AttributeSet.from_array(child1), AttributeSet.from_array(child2)