from collections import deque
from classes.Node import Node
from classes.StateUtils import StateUtils

class BFS:
    @staticmethod
    def search(initial_state):
        qty = 0
        visited_nodes = set()
        queue = deque()
        root_node = Node(None, initial_state)
        queue.append(root_node)

        while queue:
            node = queue.popleft()
            if node.state.is_solution():
                StateUtils.print_solution('BFS', qty, node)
                return True

            if node not in visited_nodes:
                visited_nodes.add(node)
                for child in node.get_children():
                    queue.append(child)

            qty += 1

        return False
