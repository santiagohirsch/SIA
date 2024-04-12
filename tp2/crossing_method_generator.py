import json
import math
import sys
from src.utils.class_utils import get_attribute_sets, get_character_class, get_crossing_method, get_cutoff_method, get_mutation_method, get_population, get_replacement_method, get_selection_method, CHARACTER_TYPES, CROSSING_METHODS
from src.utils.generator_utils import DEFAULT_MUTATION_METHOD, DEFAULT_MUTATION_RATE, DEFAULT_FIRST_SELECTION_METHOD, DEFAULT_SECOND_SELECTION_METHOD, DEFAULT_A_VALUE, DEFAULT_INDIVIDUALS, DEFAULT_CUTOFF_METHOD, DEFAULT_CUTOFF_VALUE, DEFAULT_CUTOFF_GENERATIONS, DEFAULT_REPLACEMENT_METHOD, DEFAULT_B_VALUE, DEFAULT_REPLACEMENT_FIRST_SELECTION_METHOD, DEFAULT_REPLACEMENT_SECOND_SELECTION_METHOD, DEFAULT_ATTRIBUTE_SETS
import csv


if __name__ == "__main__":



    # find mutation method class
    mutation_class = get_mutation_method(DEFAULT_MUTATION_METHOD)

    # find selection method class
    first_selection_class = get_selection_method(DEFAULT_FIRST_SELECTION_METHOD)

    second_selection_class = get_selection_method(DEFAULT_SECOND_SELECTION_METHOD)

    # find cutoff method class
    cutoff_class = get_cutoff_method(DEFAULT_CUTOFF_METHOD)

    if DEFAULT_CUTOFF_METHOD == "structure":
        cutoff_class.set_max_generations(DEFAULT_CUTOFF_GENERATIONS)
        

    # find replacement method class
    replacement_class = get_replacement_method(DEFAULT_REPLACEMENT_METHOD)
    replacement_first_selection_class = get_selection_method(DEFAULT_REPLACEMENT_FIRST_SELECTION_METHOD)
    replacement_second_selection_class = get_selection_method(DEFAULT_REPLACEMENT_SECOND_SELECTION_METHOD)
    
    # get attribute sets
    attribute_sets = get_attribute_sets(DEFAULT_ATTRIBUTE_SETS)

    with open('output/crossing_method.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Character', 'Crossing Method', 'Generation', 'Best Fitness', 'Average Fitness'])

    for character in CHARACTER_TYPES.keys():
        for crossing in CROSSING_METHODS.keys():
            # find crossing method class
            crossing_class = get_crossing_method(crossing)
            # find character class
            character_class = get_character_class(character)
            # create population
            population = get_population(attribute_sets, character)

            old_generations = []
            generation = 0
            for _ in range(50):
                
                while cutoff_class.should_cutoff(population, old_generations, generation, DEFAULT_CUTOFF_VALUE) is False:
                    
                    # select parents
                    parents = first_selection_class.select(population, math.ceil(DEFAULT_INDIVIDUALS * DEFAULT_A_VALUE))
                    parents.extend(second_selection_class.select(population, math.floor(DEFAULT_INDIVIDUALS * (1 - DEFAULT_A_VALUE))))


                    # crossing
                    children_attributes = []
                    for i in range(0, len(parents) - 1, 2): #TODO: Check
                        children_attributes.extend(crossing_class.cross(parents[i].get_attributes(), parents[i+1].get_attributes()))

                    children = []
                    # mutation
                    for child in children_attributes:
                        mutation_class.mutate(child, DEFAULT_MUTATION_RATE)
                        children.append(character_class(child))
                        

                    old_generations.append(population)
                    # replacement
                    population = replacement_class.replace(population, children, replacement_first_selection_class, replacement_second_selection_class, DEFAULT_B_VALUE)
                    generation += 1


                with open('output/crossing_method.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)

                    for i, old_generation in enumerate(old_generations):
                        best_fitness = max([individual.fitness() for individual in old_generation])
                        average_fitness = sum([individual.fitness() for individual in old_generation]) / len(old_generation)
                        writer.writerow([character, crossing, i, best_fitness, average_fitness])
