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
                print("Local Greedy solution was found opening: %d nodes" % qty)
                StateUtils.draw_solution_map(node, 0)
                return node.state
            
            if node not in visited_nodes:
                visited_nodes.add(node)
                for child in node.get_children():
                    value = Heuristics.manhattan_distance(child.state)
                    heapq.heappush(queue, AuxNode(child, value))
            
            qty += 1
        
        return None
