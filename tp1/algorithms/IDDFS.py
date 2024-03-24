from classes.Node import Node
from classes.StateUtils import StateUtils
import time

class IDDFS:
    @staticmethod
    def search(initial_state, heuristic: str = ''):
        start_time = time.time()
        depth_limit = 0
        while True:
            result, qty, frontier = IDDFS.dfs(initial_state, depth_limit)
            if result is not None:
                end_time = time.time()
                StateUtils.print_solution('IDDFS', qty, result, '', frontier)
                return True, end_time - start_time , qty , frontier
            depth_limit += 1
            if qty == -1: 
                return False, time.time() - start_time
    
    @staticmethod
    def dfs(initial_state, depth_limit):
        queue = [(Node(None, initial_state), depth_limit)]  
        qty = 0  
        while queue:
            node, depth = queue.pop()
            qty += 1  
            if node.state.is_solution():
                return node, qty, len(queue)
            if depth > 0:  
                for child in reversed(node.get_children()):
                    queue.append((child, depth - 1))  
        return None, qty, len(queue)
