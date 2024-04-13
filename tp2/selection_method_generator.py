import math
from src.utils.class_utils import get_attribute_sets, get_character_class, get_crossing_method, get_cutoff_method, get_mutation_method, get_population, get_replacement_method, get_selection_method, CHARACTER_TYPES, SELECTION_METHODS
from src.utils.generator_utils import BEST_CROSSING_METHOD, BEST_MUTATION_METHOD, BEST_MUTATION_RATE, DEFAULT_A_VALUE, DEFAULT_INDIVIDUALS, DEFAULT_CUTOFF_METHOD, DEFAULT_CUTOFF_VALUE, DEFAULT_CUTOFF_GENERATIONS, DEFAULT_REPLACEMENT_METHOD, DEFAULT_B_VALUE, DEFAULT_REPLACEMENT_FIRST_SELECTION_METHOD, DEFAULT_REPLACEMENT_SECOND_SELECTION_METHOD, DEFAULT_ATTRIBUTE_SETS
import csv


if __name__ == "__main__":

    # find crossing method class
    crossing_class = get_crossing_method(BEST_CROSSING_METHOD)

    # find mutation method class
    mutation_class = get_mutation_method(BEST_MUTATION_METHOD)

    
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

    with open('output/selection_method.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Character', 'First Selection Method', 'Second Selection Method', 'Generation', 'Best Fitness', 'Average Fitness'])

    for character in CHARACTER_TYPES.keys():
        # find character class
        character_class = get_character_class(character)
        # create population
        first_population = get_population(attribute_sets, character)
        for first_selection in SELECTION_METHODS.keys():
            # find selection method class
            first_selection_class = get_selection_method(first_selection)
            if first_selection == 'boltzmann':
                first_selection_class = first_selection_class(15, 10, 5, 50)
            elif first_selection == 'tournament_det':
                first_selection_class = first_selection_class(5)
            
            for second_selection in SELECTION_METHODS.keys():
                second_selection_class = get_selection_method(second_selection)
                if second_selection == 'boltzmann':
                    second_selection_class = second_selection_class(15, 10, 5, 50)
                elif second_selection == 'tournament_det':
                    second_selection_class = second_selection_class(5)

                for _ in range(50):
                    population = first_population
                    old_generations = []
                    generation = 0
                    
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
                            mutation_class.mutate(child, BEST_MUTATION_RATE)
                            children.append(character_class(child))
                            

                        old_generations.append(population)
                        # replacement
                        population = replacement_class.replace(population, children, replacement_first_selection_class, replacement_second_selection_class, DEFAULT_B_VALUE)
                        generation += 1


                    with open('output/selection_method.csv', 'a', newline='') as csvfile:
                        writer = csv.writer(csvfile)

                        for i, old_generation in enumerate(old_generations):
                            best_fitness = max([individual.fitness() for individual in old_generation])
                            average_fitness = sum([individual.fitness() for individual in old_generation]) / len(old_generation)
                            writer.writerow([character, first_selection, second_selection, i, best_fitness, average_fitness])

