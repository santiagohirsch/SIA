from classes.Node import Node
from classes.StateUtils import StateUtils
import time

class IDDFS:
    @staticmethod
    def search(initial_state, heuristic: str = ''):
        start_time = time.time()
        depth_limit = 0
        while True:
            result, qty = IDDFS.dfs(initial_state, depth_limit)
            if result is not None:
                end_time = time.time()
                StateUtils.print_solution('IDDFS', qty, result, heuristic)
                return True, end_time - start_time
            depth_limit += 1
            if qty == -1: 
                return False, time.time() - start_time
    
    @staticmethod
    def dfs(initial_state, depth_limit):
        stack = [(Node(None, initial_state), depth_limit)]  
        qty = 0  
        while stack:
            node, depth = stack.pop()
            qty += 1  
            if node.state.is_solution():
                return node, qty
            if depth > 0:  
                for child in reversed(node.get_children()):
                    stack.append((child, depth - 1))  
        return None, qty
