from classes.Node import Node
from classes.StateUtils import StateUtils
from algorithms import AuxNode
from algorithms.AlgorithmUtils import Heuristics
import heapq


class AStar:

    @staticmethod
    def search(initial_state):
        size = 0
        frontier = []
        heapq.heappush(frontier, AuxNode(Node(None, initial_state), 0))
        total_cost: dict[Node, float] = {Node(None, initial_state): 0}

        while frontier:
            aux = heapq.heappop(frontier)
            node = aux.node

            if node.state.is_solution():
                print("A* solution was found opening  : %d nodes", size)
                StateUtils.draw_solution_map(node, 0)
                return node.state
            
            for child in node.get_children():
                new_cost = total_cost[node] + 1
                if child not in total_cost or new_cost < total_cost[child]:
                    total_cost[child] = new_cost
                    cost = new_cost + Heuristics.manhattan_distance(child.get_state())
                    heapq.heappush(frontier, AuxNode(child, new_cost))

            size += 1
        return None
    
