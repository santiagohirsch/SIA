import importlib
import sys
from src.classes.attributes.AttributeSet import AttributeSet


CHARACTER_TYPES = {
    "archer": "Archer",
    "warrior": "Warrior",
    "defender": "Defender",
    "spy": "Spy",
}

SELECTION_METHODS = {
    "roulette": "Roulette",
    "elite": "Elite",
    "universal": "Universal",
    "tournament_det": "DeterministicTournament",
    "tournament_prob": "ProbabilisticTournament",
    "ranking": "Ranking",
    "boltzmann": "Boltzmann",
}

CROSSING_METHODS = {
    "one_point": "OnePoint",
    "two_point": "TwoPoint",
    "uniform": "Uniform",
    "anular": "Annular",
}

MUTATION_METHODS = {
    "single": "SingleMutation",
    "uniform": "UniformMultiMutation",
    "limited": "LimitedMultiMutation",
    "complete": "CompleteMutation",
}

CUTOFF_METHODS = {
    "content": "Content",
    "structure": "Structure",
    "max_gen": "MaxGenerations",
    "optimum": "OptimumEnvironment",
}

REPLACEMENT_METHODS = {
    "traditional": "Traditional",
    "young": "YoungBiased",
}

def get_population(attribute_sets, character):
    character_class = get_character_class(character)
    population = []
    for attribute_set in attribute_sets:
        population.append(character_class(attribute_set))
    return population

def get_class(class_type, class_dict, param):
    if param.lower() in class_dict:
        # find class file
        try:
            imported_module = importlib.import_module(f"src.{class_type.lower()}.{class_dict[param.lower()]}")
        except ModuleNotFoundError:
            print(f"El {class_type} {class_dict[param.lower()]} no existe o no ha sido implementado")
            sys.exit(1)

        return getattr(imported_module, class_dict[param.lower()])
    else:
        print(f"El {class_type} {param} no existe o no ha sido implementado")
        sys.exit(1)

def get_character_class(character):
    return get_class("classes.characters", CHARACTER_TYPES, character)

def get_selection_method(selection_method):
    return get_class("selection", SELECTION_METHODS, selection_method)

def get_crossing_method(crossing):
    return get_class("operators.crossing", CROSSING_METHODS, crossing)

def get_mutation_method(mutation):
    return get_class("operators.mutation", MUTATION_METHODS, mutation)

def get_cutoff_method(cutoff):
    return get_class("cutoff", CUTOFF_METHODS, cutoff)

def get_replacement_method(replacement):
    return get_class("replacement", REPLACEMENT_METHODS, replacement)

def get_attribute_sets(attribute_sets):
    sets = []
    for attribute_set in attribute_sets:
        sets.append(AttributeSet(attribute_set["agility"], attribute_set["strength"], attribute_set["expertise"], attribute_set["endurance"], attribute_set["health"], attribute_set["height"]))
    return sets
    