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
    def obtain_deadlocks(walls_points, goals_points):
        deadlocks = set()
        corners = StateUtils.__get_corners(walls_points)
        for corner in corners:
            deadlocks.update(StateUtils.__get_deadlocks_in_direction(corner, walls_points, goals_points, Movement.TOP))
            deadlocks.update(
                StateUtils.__get_deadlocks_in_direction(corner, walls_points, goals_points, Movement.LEFT))
            deadlocks.update(
                StateUtils.__get_deadlocks_in_direction(corner, walls_points, goals_points, Movement.BOTTOM))
            deadlocks.update(
                StateUtils.__get_deadlocks_in_direction(corner, walls_points, goals_points, Movement.RIGHT))

        return deadlocks

    @staticmethod
    def __check_walls_in_movements(walls_points: Set[Point], point: Point,
                                    direction1: Movement, direction2: Movement):
        return point.move(direction1) in walls_points and point.move(direction2) in walls_points

    @staticmethod
    def __get_deadlocks_in_direction(corner: Point, walls_points: Set[Point], goals_points: Set[Point],
                                     direction: Movement):
        deadlocks = []
        point = corner
        complete_walls = [True, True]
        while point not in walls_points and (complete_walls[0] or complete_walls[1]):

            if point in goals_points:
                return []

            if complete_walls[0] and point.move(Movement.orthogonal[0]) not in walls_points:
                complete_walls[0] = False

            if complete_walls[1] and point.move(Movement.orthogonal[1]) not in walls_points:
                complete_walls[1] = False

            if complete_walls[0] or complete_walls[1]:
                deadlocks.append(point)
                point = point.move(direction)
            else:
                deadlocks.clear()
        return deadlocks

    @staticmethod
    def __get_corners(walls_points: Set[Point]) -> List[Point]:
        corners = set()
        for wall in walls_points:
            if StateUtils.__check_walls_in_movements(walls_points, wall, Movement.TOP, Movement.LEFT):
                corners.add(Point.move(wall, Movement.TOP_LEFT))

            if StateUtils.__check_walls_in_movements(walls_points, wall, Movement.TOP, Movement.RIGHT):
                corners.add(Point.move(wall, Movement.TOP_RIGHT))

            if StateUtils.__check_walls_in_movements(walls_points, wall, Movement.BOTTOM, Movement.LEFT):
                corners.add(Point.move(wall, Movement.BOTTOM_LEFT))

            if StateUtils.__check_walls_in_movements(walls_points, wall, Movement.BOTTOM, Movement.RIGHT):
                corners.add(Point.move(wall, Movement.BOTTOM_RIGHT))

        return list(corners.difference(walls_points))

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
        print(f"{algorithm_name} solution was found opening: {qty} nodes\nWhen using the {get_parsed_heuristic(heuristic_name)} heuristic\nFrontier nodes: {frontier}")
        StateUtils.draw_solution_map(node, 0)

def get_parsed_heuristic(heuristic: str) -> str:
    return PARSED_HEURISTICS[heuristic]