from classes.Node import Node
from classes.StateUtils import StateUtils
from algorithms import AuxNode
from algorithms.AlgorithmUtils import Heuristics
import heapq
import time

class AStar:
    @staticmethod
    def search(initial_state):
        start_time = time.time()
        qty = 0
        frontier = []
        heapq.heappush(frontier, AuxNode(Node(None, initial_state), 0))
        total_cost = {Node(None, initial_state): 0}

        while frontier:
            aux = heapq.heappop(frontier)
            node = aux.node

            if node.state.is_solution():
                end_time = time.time()  
                duration = end_time - start_time  
                StateUtils.print_solution('A*', qty, node)
                return True, duration 
            
            for child in node.get_children():
                new_cost = total_cost[node] + 1
                if child not in total_cost or new_cost < total_cost[child]:
                    total_cost[child] = new_cost
                    cost = new_cost + Heuristics.manhattan_distance(child.get_state())
                    heapq.heappush(frontier, AuxNode(child, cost))

            qty += 1
        duration = time.time() - start_time
        return False, duration  
