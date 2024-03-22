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
                print("BFS solution was found opening: %d nodes" % qty) 
                StateUtils.draw_solution_map(node, 0)
                return node.state

            if node not in visited_nodes:
                visited_nodes.add(node)
                for child in node.get_children():
                    queue.append(child)

            qty += 1

        return None
