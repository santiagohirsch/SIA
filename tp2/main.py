import importlib
import json
import sys

from utils import get_attribute_sets, get_character_class, get_crossing_method, get_cutoff_method, get_mutation_method, get_population, get_replacement_method, get_selection_method
import math
        
def main():
    with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)
        character = config["character"]
        attribute_configs = config["attribute_sets"]
        crossing = config["crossing"]
        mutation = config["mutation"]["name"]
        mutation_rate = config["mutation"]["rate"]
        first_selection = config["selection"]["first"]
        second_selection = config["selection"]["second"]
        a_value = config["selection"]["a_value"]
        individuals = config["individuals"]
        cutoff = config["cutoff"]["name"]
        cutoff_value = config["cutoff"]["value"]
        replacement = config["replacement"]["name"]
        replacement_first_selection = config["replacement"]["selection"]["first"]
        replacement_second_selection = config["replacement"]["selection"]["second"]
        b_value = config["replacement"]["b_value"]

    # find character class
    character_class = get_character_class(character)

    # find crossing method class
    crossing_class = get_crossing_method(crossing)

    # find mutation method class
    mutation_class = get_mutation_method(mutation)

    # find selection method class
    first_selection_class = get_selection_method(first_selection)
    second_selection_class = get_selection_method(second_selection)

    # find cutoff method class
    cutoff_class = get_cutoff_method(cutoff)

    # find replacement method class
    replacement_class = get_replacement_method(replacement)

    # get attribute sets
    attribute_sets = get_attribute_sets(attribute_configs)

    # create population
    population = get_population(attribute_sets, character)

    old_generations = []
    generation = 0

    while cutoff_class.should_cutoff(population, old_generations, generation, cutoff_value) is False:
        
        # select parents
        parents = first_selection_class.select(population, math.ceil(individuals * a_value))
        parents.extend(second_selection_class.select(population, math.floor(individuals * (1 - a_value))))


        # crossing
        children_attributes = []
        for i in range(0, len(parents) - 1, 2): #TODO: Check
            children_attributes.extend(crossing_class.cross(parents[i].get_attributes(), parents[i+1].get_attributes()))

        children = []
        # mutation
        for child in children_attributes:
            mutation_class.mutate(child, mutation_rate)
            children.append(character_class(child))
            

        old_generations.append(population)
        # replacement
        population = replacement_class.replace(population, children, first_selection_class, second_selection_class, b_value)
        generation += 1

        print("Population:")
        for individual in population:
            print(individual)
            print(f"Fitness: {individual.fitness()}")



if __name__ == "__main__":
    main()