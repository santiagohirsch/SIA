import numpy as np

class Perceptron():

    def __init__(self, opt_method, activation_function = None, activation_derivative = None, weights = None):
        self.opt_method = opt_method
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.weights = weights

    def excitement(weights, training):
        return np.dot(weights, training)
    
    def activation(self, excitement):
        return self.activation_function(excitement)

    def delta(self, activation, training, expected):
        return self.opt_method.calculate(expected, activation, training, self.activation_derivative, self.excitement(self.weights, training))

    def update_weights(self, delta):
        self.weights += delta
        return self.weights

    def error(self, training_set, expected_set):
        total_error = 0
        for i in range(0, len(training_set) - 1):
            total_error += (expected_set[i] - self.activation(self.excitement(training_set[i]))) ** 2
        return total_error/2

            