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
    # 'modifiedman': 'modified_manhattan',
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
            for goal in state.goals_points:
                total_distance += abs(box.x - goal.x) + abs(box.y - goal.y)
        return total_distance

    @staticmethod
    def modified_manhattan(state: State): # defines how close you are to all boxes in the closest goal     
        print('Modified Manhattan')
        distances = [[None for _ in range(len(state.boxes_points[0]))] for _ in range(len(state.boxes_points))]
        for box in state.boxes_points:
            player_distance = abs(box.x - state.player_point.x) + abs(box.y - state.player_point.y) 
            for goal in state.goals_points:
                goal_distance = abs(box.x - goal.x) + abs(box.y - goal.y) 
                final_distance = player_distance + goal_distance
                if distances[box] is None or distances[box] > final_distance:
                    min_distance = final_distance
        min_distance = sum(filter(None, [dist for sublist in distances for dist in sublist]))
        return min_distance

    @staticmethod
    def improved_modified_manhattan(state: State): # defines how close you are to all boxes in the closest goal   
        distances = [[None for _ in range(len(state.goals_points))] for _ in range(len(state.boxes_points))]
        for i, box in enumerate(state.boxes_points):
            player_distance = abs(box.x - state.player_point.x) + abs(box.y - state.player_point.y) 
            for j, goal in enumerate(state.goals_points):
                goal_distance = abs(box.x - goal.x) + abs(box.y - goal.y) 
                distances[i][j] = player_distance + goal_distance
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