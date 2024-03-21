from classes.Node import Node
from classes.StateUtils import StateUtils
import heapq

def heuristic(state):
    player_point = state.player_point
    box_point = state.boxes_points.pop()
    state.boxes_points.add(box_point)
    goal_point = state.goals_points.pop()
    state.goals_points.add(goal_point)
    return abs(player_point.x - box_point.x) + abs(player_point.y - box_point.y) \
           + abs(box_point.x - goal_point.x) + abs(box_point.y - goal_point.y)

class AuxNode:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __str__(self):
        return f"Node: {self.node} Cost: {self.cost}"

class AStar:

    @staticmethod
    def search(initial_state):
        size = 0
        frontier = []
        heapq.heappush(frontier, AuxNode(Node(None, initial_state), 0))
        total_cost: dict[Node, float] = {Node(None, initial_state): 0}

        while frontier:
            aux_node = heapq.heappop(frontier)
            node = aux_node.node

            if node.state.is_solution():
                print("Solution found using A*! Opened nodes: ", size)
                StateUtils.draw_solution(node, 0)
                return node.state
            
            for child in node.get_children():
                new_cost = total_cost[node] + 1
                if child not in total_cost or new_cost < total_cost[child]:
                    total_cost[child] = new_cost
                    cost = new_cost + heuristic(child.getState())
                    heapq.heappush(frontier, AuxNode(child, new_cost))

            size += 1
        return None
    
