from src.operators.crossing.Crossing import Crossing
import random
from src.classes.attributes.AttributeSet import AttributeSet

class Uniform(Crossing):
    
        def cross(parent1, parent2):
            parent1_arr = parent1.to_array()
            parent2_arr = parent2.to_array()
            child1 = parent1_arr.copy()
            child2 = parent2_arr.copy()
            for i in range(len(parent1_arr)):
                if random.random() < 0.5:
                    child1[i] = parent2_arr[i]
                    child2[i] = parent1_arr[i]

            return AttributeSet.from_array(child1), AttributeSet.from_array(child2)