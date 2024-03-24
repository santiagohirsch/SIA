from collections import deque
import time
from classes.Node import Node
from classes.StateUtils import StateUtils
from classes.State import State

class DFS:
    @staticmethod
    def search(initial_state: State, heuristic: str = ''):
        start_time = time.time()
        qty = 0
        visited_nodes = set()
        queue = deque()
        root = Node(None, initial_state)
        queue.append(root)
        while queue:
            node = queue.pop()
            if node.state.is_solution():    
                end_time = time.time()
                duration = end_time - start_time    
                StateUtils.print_solution('DFS', qty, node, heuristic)
                StateUtils.print_frontier_nodes(len(queue))
                return True, duration
            if node not in visited_nodes:
                visited_nodes.add(node)
                for child in node.get_children():
                    queue.append(child)
            qty += 1
        duration = time.time() - start_time
        return False, duration