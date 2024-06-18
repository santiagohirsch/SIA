import numpy as np
from Layer import Layer

class Intermediate(Layer):

    def __init__(self, input_qty, neurons, learning_rate, activation_function, activation_derivative, weights = None):
        super().__init__(input_qty, neurons, learning_rate, activation_function, activation_derivative, weights)

    def set_deltas(self, deltas, weights):
        self.deltas = np.array([])
        for i in range(0, self.neurons):
            self.deltas = np.append(self.deltas, np.dot(deltas, weights[i]) * self.activation_derivative(self.excitement[i]))
        return self.deltas