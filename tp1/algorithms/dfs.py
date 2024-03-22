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
                print("DFS solution was found opening: %d nodes" % qty)
                StateUtils.draw_solution_map(node, 0)
                return node.state
            if node not in visited_nodes:
                visited_nodes.add(node)
                for child in node.get_children():
                    stack.append(child)
            qty += 1
        return None