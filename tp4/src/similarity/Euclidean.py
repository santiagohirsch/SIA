import numpy as np

class Euclidean:
    def similarity(self, a, b):
        return np.linalg.norm(np.array(a)-np.array(b), 2)