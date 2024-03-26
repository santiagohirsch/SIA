from classes.Direction import Direction
from classes.StateUtils import StateUtils
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
        return "Player: " + str(self.player_point) + "\nBoxes: " + str(self.boxes_points) + "\nWalls: " + str(self.walls_points) + "\nGoals: " + str(self.goals_points) + "\nDeadlocks: " + str(self.deadlocks_points) + "\n"
        

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