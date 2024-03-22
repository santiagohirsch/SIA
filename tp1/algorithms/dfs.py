from collections import deque

from classes.Node import Node
from classes.StateUtils import StateUtils


class DFS:
    @staticmethod
    def search(initial_state):
        qty = 0
        visited_nodes = set()
        stack = deque()
        root = Node(None, initial_state)
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.state.is_solution():        
                StateUtils.print_solution('DFS', qty, node)
                return True
            if node not in visited_nodes:
                visited_nodes.add(node)
                for child in node.get_children():
                    stack.append(child)
            qty += 1
        return False