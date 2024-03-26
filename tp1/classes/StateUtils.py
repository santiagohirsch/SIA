from classes.Movement import Movement
from classes.Point import Point
from typing import List, Set

PARSED_HEURISTICS = {
    'manhattan_distance': 'Manhattan Distance',
    'modified_manhattan': 'Modified Manhattan',
    'improved_modified_manhattan': 'Improved Modified Manhattan',
}

class StateUtils:
    def __init__(self):
        raise NotImplementedError("Class instantiation not supported")

    @staticmethod
    def draw_solution_map(node, depth):
        depth += 1
        if node.father is None:
            print(node.state)
            print("Depth: ", depth)
            return
        StateUtils.draw_solution_map(node.father, depth)
        print(node.state)

    @staticmethod
    def print_solution(algorithm_name, qty, node, heuristic_name, frontier):
        print(f"{algorithm_name} solution was found opening: {qty} nodes")
        if heuristic_name:
            print(f"When using the {get_parsed_heuristic(heuristic_name)} heuristic")
        print(f"Frontier nodes: {frontier}")
        StateUtils.draw_solution_map(node, 0)
        print("\n\n")

def get_parsed_heuristic(heuristic: str) -> str:
    return PARSED_HEURISTICS[heuristic]