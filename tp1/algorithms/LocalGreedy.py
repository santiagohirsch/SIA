from classes.Node import Node
from classes.StateUtils import StateUtils
from algorithms.AlgorithmUtils import AuxNode, Heuristics
import heapq

class LocalGreedy:
    @staticmethod
    def search(initial_state):
        qty = 0
        visited_nodes = set()
        queue = []
        root = Node(None, initial_state)
        heapq.heappush(queue, AuxNode(root, 0))
        
        while queue:
            aux = heapq.heappop(queue)
            node = aux.node
            
            if node.state.is_solution():
                StateUtils.print_solution('Local Greedy', qty, node)
                return True
            
            if node not in visited_nodes:
                visited_nodes.add(node)
                for child in node.get_children():
                    value = Heuristics.manhattan_distance(child.state)
                    heapq.heappush(queue, AuxNode(child, value))
            
            qty += 1
        
        return False
