from classes.Node import Node
from classes.StateUtils import StateUtils
from classes.State import State
from algorithms.AlgorithmUtils import AuxNode, Heuristics
import heapq
import time

class GlobalGreedy:
    @staticmethod
    def search(initial_state: State, heuristic: str = ''):
        start_time = time.time()
        qty = 0
        visited_nodes = set()
        queue = []
        root = Node(None, initial_state)
        heapq.heappush(queue, AuxNode(root, 0))
        heuristic_method = getattr(Heuristics, heuristic)
        
        while queue:
            aux = heapq.heappop(queue)
            node = aux.node
            
            if node.state.is_solution():
                end_time = time.time()
                duration = end_time - start_time
                StateUtils.print_solution('Global Greedy', qty, node, heuristic, len(queue))
                depth = StateUtils.calculate_depth(node)
                return True, duration , qty , len(queue), depth
            
            if node not in visited_nodes:
                visited_nodes.add(node)
                for child in node.get_children():
                    value = heuristic_method(child.state)
                    heapq.heappush(queue, AuxNode(child, value))
            
            qty += 1
        duration = time.time() - start_time
        return False, duration
