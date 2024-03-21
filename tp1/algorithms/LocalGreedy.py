from classes.Node import Node
from classes.StateUtils import StateUtils
from algorithms.AlgorithmUtils import AuxNode, Heuristics
import heapq


class LocalGreedy:
    @staticmethod
    def local_greedy(initial_state):
        size = 0
        visited = set()
        queue = []
        root = Node(None, initial_state)
        heapq.heappush(queue, AuxNode(root, 0))
        while queue:
            utility_node = heapq.heappop(queue)
            node = utility_node.node
            if node.state.is_solution():
                print("Solution found opening ", size, " nodes using Local Greedy Search")
                StateUtils.draw_solution(node, 0)
                return node.state
            if node not in visited:
                visited.add(node)
                for child in node.get_children():
                    heuristic_value = Heuristics.heuristic_manhattan_distance(child.state)
                    heapq.heappush(queue, AuxNode(child, heuristic_value))
            size += 1
        return None