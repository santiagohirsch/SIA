from abc import ABC, abstractmethod

import numpy as np

class Layer(ABC):
    def __init__(self, input_qty, output_qty, learning_rate, optimizer, activation_function = None, activation_derivative = None, weights = None):
        self.input_qty = input_qty
        self.output_qty = output_qty
        if weights is None:
            self.weights = np.array(np.random.uniform(-1, 1, size=(input_qty, output_qty)))
        else:
            self.weights = weights
        # self.activation_values = np.array([])
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        # self.deltas = np.array([])
        # self.delta_w = np.zeros((input_qty, neurons))
        self.learning_rate = learning_rate
        self.input = None
        self.output = None
        self.excitement = None
        self.optimizer = optimizer

    def activate(self, input):
        self.excitement = np.dot(input, self.weights)
        self.input = input
        # self.activation_values = np.array([])
        # for i in range(0, self.output_qty):
        #     self.activation_values = np.append(self.activation_values, self.activation_function(self.excitement[i]))
        self.output = self.activation_function(self.excitement)
        return self.output
    
    def backward(self, deltas, epoch):
        deltas = np.multiply(self.activation_derivative(self.excitement), deltas)
        input_error = np.dot(deltas, self.weights.T)
        weight_error = np.dot(self.input.T, deltas)
        # self.weights += self.optimizer.calculate(weight_error, epoch) # revisar metodos de optimizacion
        self.weights += self.learning_rate * weight_error
        return input_error
    
    def backward_no_store(self, deltas):
        deltas = np.multiply(self.activation_derivative(self.excitement), deltas)
        input_error = np.dot(deltas, np.delete(self.weights, 0, axis=0).T)
        delta_w = -np.dot(self.input.T, deltas)
        return input_error, deltas, delta_w
    
    # def test_activate(self, input):
    #     h = np.dot(input, self.weights)
    #     activation_values = np.array([])
    #     for i in range(0, self.output_qty):
    #         activation_values = np.append(activation_values, self.activation_function(h[i]))
    #     return activation_values
    
    # def get_weights(self):
    #     return self.weights
    
    # def set_weights(self, weights):
    #     self.weights = weights

    # def set_delta_w(self):
    #     for i in range(0, self.input_qty):
    #         for j in range(0, self.output_qty):
    #             self.delta_w[i][j] += self.learning_rate * self.deltas[j] * self.input[i]

    # def update_weights(self):
    #     self.weights = np.add(self.weights, self.delta_w)
    #     self.delta_w = np.zeros((self.input_qty, self.output_qty))
        