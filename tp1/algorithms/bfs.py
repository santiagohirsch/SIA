class BFS:
    @staticmethod
    def bfs(initial_state):
        visited = []
        queue = []
        steps = 0
        queue.append(initial_state)
        while queue:
            s = queue.pop(0) 
            if s.is_solution():
                print("Solution found in ", steps, " steps using BFS")
                return s
            print (s, end = " ") 
            if s not in visited:
                visited.append(s)
                for child in s.get_children():
                    queue.append(child)
            step += 1
        return None
