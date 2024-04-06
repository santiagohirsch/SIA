import random
from src.classes.attributes.AttributeSet import AttributeSet
from src.operators.mutation.Mutation import Mutation

class CompleteMutation(Mutation):
    @staticmethod
    def mutate(parent: AttributeSet, mutation_rate: float):
        parent_arr = parent.to_array()
        if mutation_rate >= random.random():
            for i in range(len(parent_arr)):
                if i == len(parent_arr) - 1:
                    parent_arr[i] = random.uniform(1.3, 2.0)
                else:
                    parent_arr[i] = random.randint(0, 150)
        return AttributeSet.from_array(parent_arr)