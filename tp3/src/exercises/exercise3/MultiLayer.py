import sys
import numpy as np
from Intermediate import Intermediate
from Output import Output


class MultiLayer:
    def __init__(self, neurons_per_layer, intermediate_func, intermediate_derivative, output_func, output_derivative, learning_rate, weights = None):
        # List of layers -> [Intermediate, Intermediate, ..., Output]  -> layers[0] = input layer -> layers[-1] = output layer
        self.layers = [] 
        for i in range(0, len(neurons_per_layer) - 1):
            if i == len(neurons_per_layer) - 2:
                rows = neurons_per_layer[i]
                cols = neurons_per_layer[i + 1]
                if weights is None:
                    self.layers.append(Output(rows, cols, learning_rate, output_func, output_derivative, np.random.uniform(-1, 1, size=(rows, cols))))
                else:
                    self.layers.append(Output(rows, cols, learning_rate, output_func, output_derivative, weights))
            else:
                rows = neurons_per_layer[i]
                cols = neurons_per_layer[i + 1]
                self.layers.append(Intermediate(rows, cols, learning_rate, intermediate_func, intermediate_derivative, np.random.uniform(-1, 1, size=(rows, cols))))

    def forward_propagation(self, input):
        for layer in self.layers:
            input = layer.activate(input)
        return input
    
    def back_propagation(self, deltas):
        self.layers[-1].set_deltas(deltas)
        for i in range(len(self.layers) - 2, -1, -1):
            deltas = self.layers[i].set_deltas(self.layers[i + 1].get_deltas(), self.layers[i + 1].get_weights())

    def update_weights(self):
        new_weights = []
        for layer in self.layers:
            layer.update_weights()
            new_weights.append(layer.get_weights())
        return new_weights
    
    def test_forward_propagation(self, input, weights = None):
        if weights is not None:
            for i in range(0, len(self.layers)):
                self.layers[i].set_weights(weights[i])
        for layer in self.layers:
            input = layer.test_activate(input)
        return input
    
    def calculate_error(self, data, expected):
        error = 0
        for i in range(0, len(data)):
            output = self.test_forward_propagation(data[i])
            for j in range(0, len(output)):
                error += ((expected[i][j] - output[j]) ** 2) / 2
        return error
    
    def set_delta_w(self):
        new_weights = []
        for layer in self.layers:
            layer.set_delta_w()
            new_weights.append(layer.get_weights())
        return new_weights
    
    def get_weights(self):
        weights = []
        for layer in self.layers:
            weights.append(layer.get_weights())
        return weights
    
    def train(self, training_data, expected_data, batch, max_epochs, epsilon, testing_data, testing_expected, metric, classes_qty):
        rows = []
        training_set = np.array(training_data)
        expected_set = np.array(expected_data)
        min_error = sys.maxsize
        all_weights = [self.layers[-1].get_weights()]
        all_errors = []
        epoch = 0
        while min_error > epsilon and epoch < max_epochs:
            training_copy = training_set.copy()
            for _ in range(0, batch):
                m = np.random.randint(0, len(training_copy) - 1)
                training_copy = np.delete(training_copy, m, 0)
                self.forward_propagation(training_set[m])
                self.back_propagation(expected_set[m])
                self.set_delta_w()
            we = self.update_weights()
            error = self.calculate_error(training_set, expected_set)
            if error < min_error:
                min_error = error
                w_min = we
            all_weights.append(we)
            all_errors.append(error)
            
            if (epoch % 1000 == 0):
                print("Epoch: ", epoch)
                training_metrics = self.calculate_metrics(training_data, expected_data, metric, w_min, classes_qty)
                test_metrics = self.calculate_metrics(testing_data, testing_expected, metric, w_min, classes_qty)
                rows.append({"epoch": epoch, "training": training_metrics, "test": test_metrics})

            epoch += 1
        return w_min, all_weights, all_errors, rows
    
    def test(self, test_data, weights):
        test_set = np.array(test_data)
        results = []
        for i in range(0, len(test_set)):
            results.append(self.test_forward_propagation(test_set[i], weights))
        return results
    
    def get_predictions(self, results):
        predictions = []
        for i, result in enumerate(results):
            if result > 0.75:
                predictions.append(i)
        if len(predictions) == 0:
            predictions.append(np.argmax(results))
        return predictions
    
    def get_expecteds(self, expected):
        expecteds = []
        for i, result in enumerate(expected):
            if result == 1:
                expecteds.append(i)
        return expecteds
            
    def confusion_matrix(self, results, expected, classes_qty):
        confusion_matrix = np.zeros((classes_qty, classes_qty))
        for i in range(len(results)):
            predictions = self.get_predictions(results[i])
            expecteds = self.get_expecteds(expected[i])
            for pred_class in predictions:
                confusion_matrix[expecteds[0]][pred_class] += 1
        return confusion_matrix

    def calculate_metrics(self, set, expected, metric, weights, classes_qty):
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0
        results = []
        for i in range(0, len(set)):
            results.append(self.test_forward_propagation(set[i], weights))
        matrix = self.confusion_matrix(results, expected, classes_qty)
        for i in range(0, classes_qty):
            for j in range(0, classes_qty):
                if i == j:
                    true_positive += matrix[i][j]
                else:
                    false_positive += matrix[i][j]
                    false_negative += matrix[j][i]
                    true_negative += matrix[j][j]
        return metric.calculate(true_positive, true_negative, false_positive, false_negative)
