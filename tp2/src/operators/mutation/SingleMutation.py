import random
from src.classes.attributes.AttributeSet import AttributeSet
from src.operators.mutation.Mutation import Mutation

class SingleMutation(Mutation):
    @staticmethod
    def mutate(parent: AttributeSet, mutation_rate: float):
        parent_arr = parent.to_array()
        last_index = len(parent_arr) - 1
        if mutation_rate >= random.random():
            random_index = random.randint(0, len(parent_arr) - 1)
            if random_index == last_index:
                parent_arr[random_index] = random.uniform(1.3, 2.0)
            else:
                parent_arr[random_index] = random.randint(0, 150)
        return AttributeSet.from_array(parent_arr)