import random
from src.classes.attributes.AttributeSet import AttributeSet
from src.operators.mutation.Mutation import Mutation

class LimitedMultiMutation(Mutation):
    @staticmethod
    def mutate(parent: AttributeSet, mutation_rate: float):
        parent_arr = parent.to_array()
        last_index = len(parent_arr) - 1
        cant_mutations = random.randint(1, last_index)
        mutated_indexes = []
        if mutation_rate >= random.random():
            for i in range(cant_mutations):
                random_index = random.randint(0, last_index)
                while random_index in mutated_indexes:
                    random_index = random.randint(0, last_index)
                mutated_indexes.append(random_index)
                if random_index == last_index:
                    parent_arr[random_index] = random.uniform(1.3, 2.0)
                else:
                    parent_arr[random_index] = random.randint(0, 150)
        return AttributeSet.from_array(parent_arr)