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
        first_selection = config["selection"]["first"]["name"]
        first_selection_params = config["selection"]["first"]["params"]
        second_selection = config["selection"]["second"]["name"]
        second_selection_params = config["selection"]["second"]["params"]
        a_value = config["selection"]["a_value"]
        individuals = config["individuals"]
        cutoff = config["cutoff"]["name"]
        cutoff_value = config["cutoff"]["value"]
        cutoff_generations = config["cutoff"]["generations"]
        replacement = config["replacement"]["name"]
        replacement_first_selection = config["replacement"]["selection"]["first"]["name"]
        replacement_first_selection_params = config["replacement"]["selection"]["first"]["params"]
        replacement_second_selection = config["replacement"]["selection"]["second"]["name"]
        replacement_second_selection_params = config["replacement"]["selection"]["second"]["params"]
        b_value = config["replacement"]["b_value"]

    # find character class
    character_class = get_character_class(character)

    # find crossing method class
    crossing_class = get_crossing_method(crossing)

    # find mutation method class
    mutation_class = get_mutation_method(mutation)

    # find selection method class
    first_selection_class = get_selection_method(first_selection)
    if first_selection == "boltzmann":
        first_selection_class = first_selection_class(first_selection_params["TC"], first_selection_params["T0"], first_selection_params["k"], first_selection_params["generation"])
    elif first_selection_class.__name__ == "DeterministicTournament":
        first_selection_class = first_selection_class(first_selection_params["k"]) 

    second_selection_class = get_selection_method(second_selection)
    if second_selection == "boltzmann":
        second_selection_class = second_selection_class(second_selection_params["TC"], second_selection_params["T0"], second_selection_params["k"], second_selection_params["generation"])
    elif second_selection_class.__name__ == "DeterministicTournament":
        second_selection_class = second_selection_class(second_selection_params["k"]) 

    # find cutoff method class
    cutoff_class = get_cutoff_method(cutoff)

    if cutoff == "structure":
        cutoff_class.set_max_generations(cutoff_generations)
        

    # find replacement method class
    replacement_class = get_replacement_method(replacement)
    replacement_first_selection_class = get_selection_method(replacement_first_selection)
    if replacement_first_selection_class.__name__ == "Boltzmann":
        replacement_first_selection_class = replacement_first_selection_class(replacement_first_selection_params["TC"], replacement_first_selection_params["T0"], replacement_first_selection_params["k"], replacement_first_selection_params["generation"])
    elif replacement_first_selection_class.__name__ == "DeterministicTournament":
        replacement_first_selection_class = replacement_first_selection_class(replacement_first_selection_params["k"]) 
    replacement_second_selection_class = get_selection_method(replacement_second_selection)
    if replacement_second_selection_class.__name__ == "Boltzmann":
        replacement_second_selection_class = replacement_second_selection_class(replacement_second_selection_params["TC"], replacement_second_selection_params["T0"], replacement_second_selection_params["k"], replacement_second_selection_params["generation"])
    elif replacement_second_selection_class.__name__ == "DeterministicTournament":
        replacement_second_selection_class = replacement_second_selection_class(replacement_second_selection_params["k"]) 

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
        population = replacement_class.replace(population, children, replacement_first_selection_class, replacement_second_selection_class, b_value)
        generation += 1

        print("-----------------------------")
        print(f"Generation {generation}")
        for individual in population:
            print(individual)
            print(f"Fitness: {individual.fitness()}")



if __name__ == "__main__":
    main()