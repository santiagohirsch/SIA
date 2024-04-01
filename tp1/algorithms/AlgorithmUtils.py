import itertools
from classes.State import State

ALGORITHMS = {
    'localgreedy': 'LocalGreedy',
    'globalgreedy': 'GlobalGreedy',
    'dfs': 'DFS',
    'astar': 'AStar',
    'bfs': 'BFS',
    'iddfs': 'IDDFS',
}

HEURISTICS = {
    'manhattan': 'manhattan_distance',
    'improvedman': 'improved_modified_manhattan'
}

class AuxNode:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f'Node: {self.node}, Priority: {self.priority}'


class Heuristics:
    @staticmethod
    def manhattan_distance(state: State):
        total_distance = 0
        for box in state.boxes_points:
            min_distance = None
            for goal in state.goals_points:
                distance = abs(box.x - goal.x) + abs(box.y - goal.y)
                if min_distance is None or distance < min_distance:
                    min_distance = distance
            total_distance += min_distance
        return total_distance

    @staticmethod
    def improved_modified_manhattan(state: State): # defines how close you are to all boxes in the closest goal   
        distances = [[None for _ in range(len(state.goals_points))] for _ in range(len(state.boxes_points))]
        for i, box in enumerate(state.boxes_points):
            # player_distance = abs(box.x - state.player_point.x) + abs(box.y - state.player_point.y) 
            box_in_goal = False
            for j, goal in enumerate(state.goals_points):
                goal_distance = abs(box.x - goal.x) + abs(box.y - goal.y) 
                if goal_distance == 0 or box_in_goal:
                    box_in_goal = True
                    distances[i][j] = 0
                else:
                    distances[i][j] = goal_distance
        return minor_sum(distances)

        

def algorithm_normalizer(algorithm: str) -> str:
    # first I remove the extension if provided any
    algorithm = algorithm.replace('.py', '')
    # then I remove the path if provided any
    algorithm = algorithm.split('/')[-1]
    if algorithm.lower() in ALGORITHMS:
        return ALGORITHMS[algorithm.lower()]
    else:
        return None

def heuristic_normalizer(heuristic: str) -> str:
    if heuristic.lower() in HEURISTICS:
        return HEURISTICS[heuristic.lower()]
    else:
        return None

def minor_sum(matriz):
    n = len(matriz)
    minor_sum = float('inf')
    
    # Generar todas las permutaciones posibles de las columnas
    cols = list(range(n))
    cols_exanges = itertools.permutations(cols)
    
    # Iterar sobre todas las permutaciones posibles
    for exanges in cols_exanges:
        actual_sum = sum(matriz[i][exanges[i]] for i in range(n))
        minor_sum = min(minor_sum, actual_sum)
    
    return minor_sum