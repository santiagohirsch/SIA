from classes.Direction import Direction
from classes.StatePrinter import StatePrinter
from classes.Point import Point

class State:
    def __init__(self, boxes_points: Point, walls_points: Point, player_point: Point, goals_points: Point, deadlocks_points: Point):
        self.walls_points = walls_points
        self.player_point = player_point
        self.goals_points = goals_points
        self.boxes_points = boxes_points
        self.deadlocks_points = deadlocks_points
        self._hash_value = None
        
    def __str__(self):
        object_symbols = {
            'wall': '#',
            'player': 'P',
            'goal': 'O',
            'box': 'B',
            'box_positioned': '*',
            'player_positioned': 'x'
        }

        all_points = [
            self.player_point,
            *self.boxes_points,
            *self.walls_points,
            *self.goals_points
        ]

        max_x = max(point.x for point in all_points) + 1
        max_y = max(point.y for point in all_points) + 1

        boxes_on_goals = [point for point in self.boxes_points if point in self.goals_points]
        boxes = [point for point in self.boxes_points if point not in boxes_on_goals]
        player_symbol = object_symbols['player_positioned'] if self.player_point in self.goals_points else object_symbols['player']

        builder = StatePrinter(max_x, max_y)
        builder.add_points(self.walls_points, object_symbols['wall']) \
            .add_points(self.goals_points, object_symbols['goal']) \
            .add_points(boxes_on_goals, object_symbols['box_positioned']) \
            .add_points(boxes, object_symbols['box']) \
            .add_points([self.player_point], player_symbol)

        return str(builder)
        

    def __hash__(self):
        if self._hash_value is None:
            self._hash_value = hash((tuple(self.boxes_points), self.player_point))
        return self._hash_value

    def __eq__(self, other):
        return self.player_point == other.player_point and self.boxes_points == other.boxes_points
    
    def can_continue_search(self, direction):
        return self.can_move(direction)

    def can_move(self, direction):
        next_point = self.player_point.move(direction)
        if next_point in self.walls_points:
            return 0
        if next_point in self.boxes_points:
            next_box_point = next_point.move(direction)
            if next_box_point in self.walls_points or next_box_point in self.boxes_points or next_box_point in self.deadlocks_points:
                return 0
            return 1
        return 2

    def has_deadlocks(self, point):
        return point not in self.deadlocks_points

    def move(self, direction):
        if self.is_solution():
            print("Solution found :)")
            return

        can_continue_search = self.can_continue_search(direction)
        if can_continue_search != 0:
            next_point = self.player_point.move(direction)
            if can_continue_search == 1:
                next_box_point = next_point.move(direction)
                new_boxes_points = self.boxes_points.copy()
                new_boxes_points.remove(next_point)
                new_boxes_points.add(next_box_point)
                return State(new_boxes_points, self.walls_points, next_point, self.goals_points, self.deadlocks_points)
            return State(self.boxes_points, self.walls_points, next_point, self.goals_points, self.deadlocks_points)

    def get_children(self):
        children = []
        for direction in Direction:
            if self.can_continue_search(direction):
                children.append(self.move(direction))
        return children

    def is_solution(self):
        return self.boxes_points.issubset(self.goals_points)