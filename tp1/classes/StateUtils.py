from classes.Direction import Direction
from classes.Point import Point


class StateUtils:
    def __init__(self):
        raise NotImplementedError("Class instantiation not supported")

    # A deadlock occurs when :
    #   - We are in a corner
    #   - We are between two deadlocks, next to two walls which don't have holes
    @staticmethod
    def obtain_deadlocks(walls_points, goals_points):
        deadlocks = []

        for wall in walls_points:
            maybe_corner = StateUtils.__get_corner_or_none(walls_points, wall)
            if maybe_corner is not None:
                if maybe_corner not in goals_points:  # corner
                    deadlocks.append(maybe_corner)

        # we may have received wall points as corners, so we need to get rid of them
        return set(deadlocks).difference(walls_points)

    @staticmethod
    def __get_corner_or_none(walls_points, point: Point):
        return (point.move(Direction.TOP) in walls_points or point.move(Direction.BOTTOM) in walls_points) \
            and (point.move(Direction.LEFT) or point.move(Direction.RIGHT))

    @staticmethod
    def draw_solution(node, depth):
        depth += 1
        if node.father is None:
            print("Depth: ", depth)
            print(node.state)
            return
        StateUtils.draw_solution(node.father, depth)
        print(node.state)