import itertools
from classes.Point import Point
from typing import List, Set
from classes.State import State


PARSED_HEURISTICS = {
    'manhattan_distance': 'Manhattan Distance',
    'improved_modified_manhattan': 'Improved Modified Manhattan',
}

class StateUtils:
    def __init__(self):
        raise NotImplementedError("Class instantiation not supported")
    
    @staticmethod
    def calculate_depth(node):
        depth = 0
        while node.father is not None:
            node = node.father
            depth += 1
        return depth

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