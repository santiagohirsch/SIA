import sys
import importlib
from classes.SokobanUtils import SokobanUtils
from algorithms.AlgorithmUtils import algorithm_normalizer
from algorithms.AlgorithmUtils import heuristic_normalizer
from algorithms.AlgorithmUtils import ALGORITHMS
from classes.State import State
from algorithms.AlgorithmUtils import HEURISTICS
import csv



if __name__ == "__main__":

    map_path = 'maps/map2.txt'
    try:
        with open(map_path, 'r') as file:
            sokoban_board = file.read()
    except FileNotFoundError:
        print(f"Error: Map {map_path} not found.")

    parsed_positions = SokobanUtils.parse_sokoban_board(sokoban_board)

    walls = parsed_positions.get('wall', [])
    blanks = parsed_positions.get('blank', [])
    boxes = parsed_positions.get('box', [])
    player = parsed_positions.get('player', [])[0]
    goals = parsed_positions.get('goal', [])
    deadlocks = SokobanUtils.get_deadlocks(walls, blanks)
    with open('results2.csv', 'a', newline='') as file:
        writer = csv.writer(file)  
        writer.writerow(['Algorithm', 'Duration', 'Nodes Expanded', 'Frontier Nodes', 'Heuristic'])

    for algorithm in ALGORITHMS:
        if(algorithm == 'iddfs'):
            continue
        for heuristic in HEURISTICS:
            for _ in range(100):
                    try:
                        imported_module = importlib.import_module(f"algorithms.{algorithm_normalizer(algorithm)}")
                    except ModuleNotFoundError:
                        sys.exit(1)
                    algorithm_class = getattr(imported_module, algorithm_normalizer(algorithm))
                    success, duration, nodes, frontier_nodes = algorithm_class.search(State(set(boxes), set(walls), player, set(goals), set(deadlocks)), heuristic_normalizer(heuristic))
                    with open('results2.csv', 'a', newline='') as file:
                        writer = csv.writer(file)  
                        writer.writerow([algorithm, duration, nodes, frontier_nodes, heuristic])




