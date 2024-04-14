DEFAULT_CROSSING_METHOD = 'one_point'
DEFAULT_MUTATION_METHOD = 'limited'
DEFAULT_MUTATION_RATE = 0.8
DEFAULT_FIRST_SELECTION_METHOD = 'roulette'
DEFAULT_SECOND_SELECTION_METHOD = 'elite'
DEFAULT_A_VALUE = 0.5
DEFAULT_INDIVIDUALS = 100
DEFAULT_CUTOFF_METHOD = 'structure'
DEFAULT_CUTOFF_VALUE = 0.8
DEFAULT_CUTOFF_GENERATIONS = 50
DEFAULT_REPLACEMENT_METHOD = 'traditional'
DEFAULT_B_VALUE = 0.7
DEFAULT_REPLACEMENT_FIRST_SELECTION_METHOD = 'roulette'
DEFAULT_REPLACEMENT_SECOND_SELECTION_METHOD = 'elite'
DEFAULT_ATTRIBUTE_SETS = [
        {"agility": 15, "strength":  25, "expertise": 35, "endurance": 40, "health": 35, "height": 1.6 },
        {"agility": 20, "strength":  30, "expertise": 30, "endurance": 35, "health": 35, "height": 1.5 },
        {"agility": 25, "strength":  35, "expertise": 25, "endurance": 30, "health": 35, "height": 1.7 },
        {"agility": 30, "strength":  40, "expertise": 20, "endurance": 25, "health": 35, "height": 1.8 },
        {"agility": 35, "strength":  45, "expertise": 15, "endurance": 20, "health": 35, "height": 2.0 },
        {"agility": 40, "strength":  50, "expertise": 10, "endurance": 15, "health": 35, "height": 1.3 },
        {"agility": 45, "strength":  55, "expertise": 5, "endurance": 10, "health": 35, "height": 1.9 },
        {"agility": 50, "strength":  60, "expertise": 0, "endurance": 5, "health": 35, "height": 1.4 },
        {"agility": 55, "strength":  55, "expertise": 5, "endurance": 5, "health": 30, "height": 1.6 },
        {"agility": 60, "strength":  50, "expertise": 10, "endurance": 5, "health": 25, "height": 1.8 }
    ]
BEST_CROSSING_METHOD = 'uniform'
BEST_MUTATION_METHOD = 'single'
BEST_MUTATION_RATE = 0.55
BEST_FIRST_SELECTION_METHOD = 'tournament_prob'
BEST_SECOND_SELECTION_METHOD = 'roulette'