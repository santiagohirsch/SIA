from classes.Node import Node
from classes.StateUtils import StateUtils
from algorithms.AlgorithmUtils import AuxNode, Heuristics
from classes.State import State
import heapq
import time

class LocalGreedy:
    @staticmethod
    def search(initial_state: State):
        start_time = time.time()
        qty = 0
        visited_nodes = set()
        queue = []
        root = Node(None, initial_state)
        heapq.heappush(queue, AuxNode(root, 0))
        
        while queue:
            aux = heapq.heappop(queue)
            node = aux.node
            
            if node.state.is_solution():
                end_time = time.time()
                duration = end_time - start_time
                StateUtils.print_solution('Local Greedy', qty, node)
                return True, duration
            
            if node not in visited_nodes:
                visited_nodes.add(node)
                sorted_children = sorted(node.get_children(), key=lambda child: Heuristics.manhattan_distance(child.state))
                for child in sorted_children:
                    heapq.heappush(queue, AuxNode(child, Heuristics.manhattan_distance(child.state)))
            
            qty += 1
        duration = time.time() - start_time
        return False, duration
