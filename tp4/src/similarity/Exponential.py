import numpy as np

class Exponential:
    def similarity(self, x, y):
        return np.exp(-np.linalg.norm(x - y, 2)**2)