import numpy as np
import sys
import random

class Perceptron():

    def __init__(self, weights_qty, opt_method,learning_rate, activation_function = None, activation_derivative = None, weights = None):
        self.opt_method = opt_method
        self.learning_rate = learning_rate
        self.opt_method.configure(learning_rate)
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        if weights is None:
            self.weights = np.random.uniform(-1, 1, (1, weights_qty))[0]
        else:
            self.weights = weights

    def excitement(self, weights, training):
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
            total_error += (expected_set[i] - self.activation(self.excitement(self.weights,training_set[i]))) ** 2
        return total_error/2

    def train(self, training_set, expected_set, batch, epoch, epsilon):
        training_set = np.array(training_set)
        training_errors = []
        min_error = sys.maxsize
        w_min = None
        i = 0
        while (min_error > epsilon and i < epoch):
            training_copy = np.array(training_set.copy())
            expected_copy = expected_set.copy()
            delta = [0.0 for i in range(len(self.weights))]
            for _ in range(0, batch):
                m = random.randint(0, len(training_copy) - 1)
                excitement = self.excitement(self.weights, training_copy[m])
                activation = self.activation(excitement)
                expected = expected_copy.pop(m)
                delta += self.delta(activation, training_copy[m], expected)
                training_copy = np.delete(training_copy,m,0)
                #expected_copy.pop(m)
            self.update_weights(delta)
            error = self.error(training_set, expected_set)
            if error < min_error:
                min_error = error
                w_min = self.weights
            training_errors.append(error)
            i += 1
        return w_min, training_errors
    
    def test(self, test_set, weights):
        initial_weights = self.weights
        self.weights = weights
        results = []
        for i in range(0, len(test_set)):
            excitement = self.excitement(self.weights, test_set[i])
            results.append(self.activation(excitement))
        self.weights = initial_weights
        return results