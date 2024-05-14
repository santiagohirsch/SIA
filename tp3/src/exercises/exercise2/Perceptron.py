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
            self.weights = np.array(np.random.uniform(-1, 1, size=(1, weights_qty + 1)))
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
            copy = []
            copy.append(1)
            for j in range(0, len(training_set[i])):
                copy.append(training_set[i][j])
            total_error += (expected_set[i] - self.activation(self.excitement(copy))) ** 2
        return total_error * 0.5

    def test_error(self, test_set, expected_set, weights):
        total_error = 0
        for i in range(0, len(test_set) - 1):
            copy = []
            copy.append(1)
            for j in range(0, len(test_set[i])):
                copy.append(test_set[i][j])
            total_error += (expected_set[i] - self.activation(self.test_excitement(copy, weights))) ** 2
        return total_error * 0.5
    
    def test_excitement(self, test_set, w):
        return np.dot(w, test_set)


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
                copy = []
                copy.append(1)
                for z in range(0, len(training_value)):
                    copy.append(training_value[z])
                excitement = self.excitement(copy)
                activation = self.activation(excitement)
                delta += self.calculate_delta(activation, np.array(copy), expected)
            w = self.update_weights(delta)
            error = self.error(training_set, expected_set)
            if error < min_error:
                min_error = error
                w_min = w
            training_errors.append(error)
            test_errors.append(self.test_error(test_set_copy, test_expected_copy, w_min)) 
            limit += 1
            if i == k-1:
                i = 0
            else:
                i += 1

        return w_min, training_errors, test_errors
    
    def k_test(self, k, training_set, expected_set, epoch, epsilon, shuffle = False, batch = 1):
        training_set_aux = np.array(training_set)
        expected_set_aux = np.array(expected_set)  # Create a copy to avoid modifying the original
        training_errors_set = []
        test_errors_set = []
        
        if shuffle:
            sorted_arrays = []
            sorted_expected = []
            
            for _ in range(len(training_set_aux)):
                random_index = random.randint(0, len(training_set_aux) - 1)
                sorted_arrays.append(training_set_aux[random_index])
                sorted_expected.append(expected_set_aux[random_index])
                
                # Remove selected items by slicing
                training_set_aux = np.delete(training_set_aux, random_index, axis=0)
                expected_set_aux = np.delete(expected_set_aux, random_index)
            
            # Overwrite training_set_aux and expected_set with the new arrays
            training_set_aux = np.array(sorted_arrays)
            expected_set_aux = np.array(sorted_expected)


        for i in range(k):
            fold_size = len(training_set_aux) // k
            index_start = i * fold_size
            index_end = (i + 1) * fold_size

            test_set_copy = training_set_aux[index_start:index_end]
            test_expected_copy = expected_set_aux[index_start:index_end]

            training_copy = np.concatenate((training_set_aux[:index_start], training_set_aux[index_end:]), axis=0)
            expected_copy = np.concatenate((expected_set_aux[:index_start], expected_set_aux[index_end:]), axis=0).tolist()
            if batch > len(training_copy):
                batch = len(training_copy)
            w_min, training_errors = self.train(training_copy, expected_copy, batch, epoch, epsilon)

            training_errors_set.append(training_errors)
            test_errors_set.append(self.test_error(test_set_copy, test_expected_copy, w_min))
            # print("k: ", i)
            # print("training_errors: ", training_errors)
            # print("--------------------")

        return w_min, training_errors_set, test_errors_set


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
                copy = []
                copy.append(1)
                for z in range(0, len(training_value)):
                    copy.append(training_value[z])
                excitement = self.excitement(copy)
                activation = self.activation(excitement)
                delta += self.calculate_delta(activation, np.array(copy), expected)
            # print('epoch: ', i) 
            we = self.update_weights(delta)
            error = self.error(training_set, expected_set)
            # print('error: ', error)
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
            copy = []
            copy.append(1)
            for j in range(0, len(test_set[i])):
                copy.append(test_set[i][j])
            excitement = self.excitement(copy)
            results = np.append(results, self.activation(excitement))
        self.weights = initial_weights
        return results