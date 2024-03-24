from classes.Node import Node
from classes.State import State
from classes.StateUtils import StateUtils
from algorithms.AlgorithmUtils import AuxNode
from algorithms.AlgorithmUtils import Heuristics
import heapq
import time

class AStar:
    @staticmethod
    def search(initial_state: State, heuristic: str = ''):
        start_time = time.time()
        qty = 0
        queue = []
        heapq.heappush(queue, AuxNode(Node(None, initial_state), 0))
        total_cost = {Node(None, initial_state): 0}
        heuristic_method = getattr(Heuristics, heuristic)

        while queue:
            aux = heapq.heappop(queue)
            node = aux.node

            if node.state.is_solution():
                end_time = time.time()  
                duration = end_time - start_time  
                StateUtils.print_solution('A*', qty, node, heuristic, len(queue))
                return True, duration 
            
            for child in node.get_children():
                new_cost = total_cost[node] + 1
                if child not in total_cost or new_cost < total_cost[child]:
                    total_cost[child] = new_cost
                    cost = new_cost + heuristic_method(child.get_state())
                    heapq.heappush(queue, AuxNode(child, cost))

            qty += 1
        duration = time.time() - start_time
        return False, duration  
