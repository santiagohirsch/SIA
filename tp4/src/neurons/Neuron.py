from abc import ABC, abstractmethod

class Neuron(ABC):
    def get_weights(self):
        return self.weights
    
    def set_weights(self, weights):
        self.weights = weights.copy()