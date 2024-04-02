import sys
import importlib
from classes.SokobanUtils import SokobanUtils
from algorithms.AlgorithmUtils import algorithm_normalizer
from algorithms.AlgorithmUtils import heuristic_normalizer
from classes.State import State
from algorithms.AlgorithmUtils import HEURISTICS

if __name__ == "__main__":
    # Set algorithm and map as None
    options = {'algorithm': None, 'map': None, 'heuristic': None}

    # Run through params to find algorithm and map
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '-a' or sys.argv[i] == '--algorithm':
            options['algorithm'] = sys.argv[i+1]
        elif sys.argv[i] == '-m' or sys.argv[i] == '--map':
            options['map'] = sys.argv[i+1]
        elif sys.argv[i] == '-h' or sys.argv[i] == '--heuristic':
            options['heuristic'] = sys.argv[i+1]
        i += 2

    # Check if parameters where received
    if options['algorithm'] is None or options['map'] is None:
        print("Program was executed incorrectly please check readme file for instructions.")
        exit(1)
    
    normalized_algorithm = algorithm_normalizer(options['algorithm'])
    normalized_heuristic = None
    if options['heuristic'] is not None:
        normalized_heuristic = heuristic_normalizer(options['heuristic'])
    # find map file
    try:
        with open(options['map'], 'r') as file:
            sokoban_board = file.read()
    except FileNotFoundError:
        print(f"Error: Map {options['map']} not found.")
        sys.exit(1)

    # find algorithm file
    try:
        imported_module = importlib.import_module(f"algorithms.{normalized_algorithm}")
    except ModuleNotFoundError:
        print(f"El algoritmo {normalized_algorithm if normalized_algorithm is not None else options['algorithm']} no existe o no ha sido implementado")
        sys.exit(1)

    parsed_positions = SokobanUtils.parse_sokoban_board(sokoban_board)

    walls = parsed_positions.get('wall', [])
    blanks = parsed_positions.get('blank', [])
    boxes = parsed_positions.get('box', [])
    player = parsed_positions.get('player', [])[0]
    goals = parsed_positions.get('goal', [])
    deadlocks = SokobanUtils.get_deadlocks(walls, blanks)

    algorithm_class = getattr(imported_module, normalized_algorithm)
    print("Solving...")
    if normalized_heuristic is None and normalized_algorithm != 'IDDFS' and normalized_algorithm != 'BFS' and normalized_algorithm != 'DFS':
        for _, heuristic in HEURISTICS.items():
            success, duration, nodes, frontier_nodes = algorithm_class.search(State(set(boxes), set(walls), player, set(goals), set(deadlocks)), heuristic)
            if success:
                print(f"It took {round(duration, 9)} seconds to solve the map: {options['map'].split('/')[-1]}")
            else:
                print(f"Failure, could not solve the map: {options['map'].split('/')[-1]}")
    else:
        success, duration, nodes, frontier_nodes, _ = algorithm_class.search(State(set(boxes), set(walls), player, set(goals), set(deadlocks)), normalized_heuristic)
        if success:
            print(f"It took {round(duration, 9)} seconds to solve the map: {options['map'].split('/')[-1]}")
        else:
            print(f"Failure, could not solve the map: {options['map'].split('/')[-1]}")
