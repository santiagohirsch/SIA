from collections import deque
import time
from classes.Node import Node
from classes.StateUtils import StateUtils


class DFS:
    @staticmethod
    def search(initial_state):
        start_time = time.time()
        qty = 0
        visited_nodes = set()
        stack = deque()
        root = Node(None, initial_state)
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.state.is_solution():    
                end_time = time.time()
                duration = end_time - start_time    
                StateUtils.print_solution('DFS', qty, node)
                return True, duration
            if node not in visited_nodes:
                visited_nodes.add(node)
                for child in node.get_children():
                    stack.append(child)
            qty += 1
        duration = time.time() - start_time
        return False, duration