from abc import ABC, abstractmethod

import numpy as np

class Layer(ABC):
    def __init__(self, input_qty, neurons, learning_rate, activation_function = None, activation_derivative = None, weights = None):
        self.input_qty = input_qty
        self.neurons = neurons
        if weights is None:
            self.weights = np.array(np.random.uniform(-1, 1, size=(input, neurons)))
        else:
            self.weights = weights
        self.activation_values = np.array([])
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.deltas = np.array([])
        self.delta_w = np.zeros((input_qty, neurons))
        self.learning_rate = learning_rate
        self.input = None
        self.h = None

    def activate(self, input):
        self.h = np.dot(input, self.weights)
        self.input = input
        self.activation_values = np.array([])
        for i in range(0, self.neurons):
            self.activation_values = np.append(self.activation_values, self.activation_function(h[i]))
        return self.activation_values
    
    def test_activate(self, input):
        h = np.dot(input, self.weights)
        activation_values = np.array([])
        for i in range(0, self.neurons):
            activation_values = np.append(activation_values, self.activation_function(h[i]))
        return activation_values
    
    def get_deltas(self):
        return self.deltas
    
    def get_weights(self):
        return self.weights
    
    def set_weights(self, weights):
        self.weights = weights

    def set_delta_w(self):
        for i in range(0, self.input_qty):
            for j in range(0, self.neurons):
                self.delta_w[i][j] = self.learning_rate * self.deltas[j] * self.activation_derivative(self.h[j]) * self.input[i]

    def update_weights(self):
        self.weights = np.add(self.weights, self.delta_w)
        self.delta_w = np.zeros((self.input_qty, self.neurons))
        
