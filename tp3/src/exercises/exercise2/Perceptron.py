import numpy as np
import sys
import random

class Perceptron():

    def __init__(self, weights_qty, opt_method, learning_rate, activation_function = None, activation_derivative = None, weights = None):
        self.learning_rate = learning_rate
        self.opt_method = opt_method
        self.opt_method.configure(learning_rate)
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        if weights is None:
            self.weights = np.array(np.random.uniform(0, 1, size=(1, weights_qty)))
        else:
            self.weights = np.array(weights)

    def excitement(self, training):
        return np.dot(self.weights, training)
    
    def activation(self, excitement):
        return self.activation_function(excitement)

    def calculate_delta(self, activation, training, expected):
        return self.opt_method.calculate(expected, activation, training, self.activation_derivative, self.excitement(training))

    def update_weights(self, delta):
        self.weights = self.weights + delta
        return self.weights

    def error(self, training_set, expected_set):
        total_error = 0
        for i in range(0, len(training_set) - 1):
            total_error += (expected_set[i] - self.activation(self.excitement(training_set[i]))) ** 2
        return total_error * 0.5
    

    def k_fold_cross_validation(self, k, training_set, expected_set, epoch, epsilon):
        if k <= 1 or k >= len(training_set):
            raise ValueError('K value must be lower than the training set size and greater than 1.')
        training_errors = []
        test_errors = []
        min_error = sys.maxsize
        w_min = None
        i = 0
        limit = 0
        min_error = sys.maxsize
        w_min = None
        training_set_aux = np.array(training_set)

        while(limit < epoch and min_error > epsilon):
            fold_size = len(training_set_aux) // k
            index_start = i * fold_size
            index_end = (i + 1) * fold_size


            test_set_copy = training_set_aux[index_start:index_end]
            test_expected_copy = expected_set[index_start:index_end]

            training_copy = np.concatenate((training_set_aux[:index_start], training_set_aux[index_end:]), axis=0)
            expected_copy = np.concatenate((expected_set[:index_start], expected_set[index_end:]), axis=0).tolist()
            delta = [0.0 for _ in range(len(self.weights[0]))]

            for _ in range(0, k):
                m = random.randint(0, len(training_copy) - 1)
                training_value = training_copy[m]
                training_copy = np.delete(training_copy,m,0)
                expected = expected_copy.pop(m)
                excitement = self.excitement(training_value)
                activation = self.activation(excitement)
                delta += self.calculate_delta(activation, np.array(training_value), expected)
            w = self.update_weights(delta)
            error = self.error(training_set, expected_set)
            if error < min_error:
                min_error = error
                w_min = w
            training_errors.append(error)
            test_errors.append(self.error(test_set_copy, test_expected_copy))
            limit += 1
            if i == k-1:
                i = 0
            else:
                i += 1

        return w_min, training_errors, test_errors

    def train(self, training_set, expected_set, batch, epoch, epsilon):
        # training_set = np.array(training_set)
        training_errors = []
        min_error = sys.maxsize
        w_min = None
        i = 0
        while (min_error > epsilon and i < epoch):
            training_copy = np.array(training_set.copy())
            expected_copy = expected_set.copy()
            delta = [0.0 for _ in range(len(self.weights[0]))]
            for _ in range(0, batch):
                m = random.randint(0, len(training_copy) - 1)
                training_value = training_copy[m]
                training_copy = np.delete(training_copy,m,0)
                expected = expected_copy.pop(m)
                excitement = self.excitement(training_value)
                activation = self.activation(excitement)
                delta += self.calculate_delta(activation, np.array(training_value), expected)
            print('epoch: ', i) 
            we = self.update_weights(delta)
            error = self.error(training_set, expected_set)
            print('error: ', error)
            if error < min_error:
                min_error = error
                w_min = we
            training_errors.append(min_error)
            i += 1

        return w_min, training_errors
    
    def test(self, test_set, weights):
        initial_weights = self.weights.copy()
        self.weights = weights
        results = np.array([])
        for i in range(0, len(test_set)):
            excitement = self.excitement(test_set[i])
            results = np.append(results, self.activation(excitement))
        self.weights = initial_weights
        return results