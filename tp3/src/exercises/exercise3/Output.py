import numpy as np
from Layer import Layer

class Output(Layer):

    def __init__(self, input_qty, neurons, learning_rate, activation_function, activation_derivative, weights = None):
        super().__init__(input_qty, neurons, learning_rate, activation_function, activation_derivative, weights)

    def set_deltas(self, expected_output):
        self.deltas = np.array([])
        for i in range(0, self.neurons):
            self.deltas = np.append(self.deltas, (expected_output[i] - self.activation_values[i]) * self.activation_derivative(self.excitement[i]))
        return self.deltas