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
            Aux = heapq.heappop(queue)
            node = Aux.node
            if node.state.is_solution():
                print("Local Greedy Search opened %d nodes", size)
                StateUtils.draw_solution_map(node, 0)
                return node.state
            if node not in visited:
                visited.add(node)
                for child in node.get_children():
                    value = Heuristics.manhattan_distance(child.state)
                    heapq.heappush(queue, AuxNode(child, value))
            size += 1
        return None