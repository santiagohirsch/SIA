import random
import sys
import numpy as np
import pandas as pd
from Intermediate import Intermediate
from Output import Output
from Accuracy import Accuracy
from F1 import F1
from Precision import Precision
from Recall import Recall

metric_functions = {
'F1': F1,
'recall': Recall,
'precision': Precision,
'accuracy': Accuracy
}

class MultiLayer:
    def __init__(self, neurons_per_layer, intermediate_func, intermediate_derivative, output_func, output_derivative, learning_rate, weights = None):
        # List of layers -> [Intermediate, Intermediate, ..., Output]  -> layers[0] = input layer -> layers[-1] = output layer
        self.layers = [] 
        for i in range(0, len(neurons_per_layer) - 1):
            if i == len(neurons_per_layer) - 2:
                rows = neurons_per_layer[i] + 1
                cols = neurons_per_layer[i + 1]
                if weights is None:
                    self.layers.append(Output(rows, cols, learning_rate, output_func, output_derivative, np.random.uniform(-1, 1, size=(rows, cols))))
                else:
                    self.layers.append(Output(rows, cols, learning_rate, output_func, output_derivative, weights))
            else:
                rows = neurons_per_layer[i] + 1
                cols = neurons_per_layer[i + 1]
                self.layers.append(Intermediate(rows, cols, learning_rate, intermediate_func, intermediate_derivative, np.random.uniform(-1, 1, size=(rows, cols))))

    def forward_propagation(self, input):
        # print("input: ", input)
        for layer in self.layers:
            input_copy = []
            input_copy.append(1)
            for i in range(0, len(input)):
                input_copy.append(input[i])
            # print("input_copy: ", input_copy)
            input = layer.activate(input_copy)
        return input
    
    def back_propagation(self, deltas):
        self.layers[-1].set_deltas(deltas)
        for i in range(len(self.layers) - 2, -1, -1):
            deltas = self.layers[i].set_deltas(self.layers[i + 1].get_deltas(), self.layers[i + 1].get_weights()[1:])

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
            input_copy = []
            input_copy.append(1)
            for i in range(0, len(input)):
                input_copy.append(input[i])
            input = layer.test_activate(input_copy)
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
        # f1 = []
        # accuracy = []
        # precision = []
        # recall = []

        metrics_data = {metric_name: [] for metric_name in metric_functions.keys()}  # Inicializa el diccionario con listas vacías para cada métrica

        training_set = np.array(training_data)
        expected_set = np.array(expected_data)
        min_error = sys.maxsize
        all_weights = [self.layers[-1].get_weights()]
        all_errors = []
        epoch = 0
        while min_error > epsilon and epoch < max_epochs:
            training_copy = training_set.copy()
            for _ in range(0, batch):
                m = np.random.randint(0, len(training_copy))
                training_copy = np.delete(training_copy, m, 0)
                self.forward_propagation(training_set[m])
                self.back_propagation(expected_set[m])
                self.set_delta_w()
            we = self.update_weights()
            error = self.calculate_error(training_set, expected_set)
            # print("Epoch: ", epoch, "Error: ", error)
            if error < min_error:
                min_error = error
                w_min = we
            all_weights.append(we)
        
            if (epoch % 100 == 0 and epoch != 0):
                print(f"Epoch: {epoch}, Error: {error}")
                all_errors.append(error)
                # for metric_name, metric in metric_functions.items():
                #     training_metrics = self.calculate_metrics(training_data, expected_data, metric, w_min, classes_qty)
                #     test_metrics = self.calculate_metrics(testing_data, testing_expected, metric, w_min, classes_qty)
                #     metrics_data[metric_name].append({"epoch": epoch, "training": training_metrics, "test": test_metrics})

            epoch += 1
        all_errors.append(min_error)


        errors_df = pd.DataFrame({'Epoch': [i*100 for i in range(len(all_errors))], 'Error': all_errors})
        errors_df.to_csv('betas3.csv', index=False)
        for metric_name, metric in metric_functions.items():
            test_metrics = self.calculate_metrics(testing_data, testing_expected, metric, w_min, classes_qty)
            print(f"Test {metric_name}: {test_metrics}")
        print(pd.DataFrame(metrics_data))
        return w_min, all_weights, all_errors, []
    
    def test(self, test_data, weights):
        test_set = np.array(test_data)
        results = []
        for i in range(0, len(test_set)):
            results.append(self.test_forward_propagation(test_set[i], weights))
        return results
    
    def get_predictions(self, results):
        predictions = []
        for i, result in enumerate(results):
            if result > 0.5:
                predictions.append(i)
        return predictions
    
    def get_expecteds(self, expected):
        expecteds = []
        for i, result in enumerate(expected):
            if result == 1:
                expecteds.append(i)
        return expecteds
            
    def confusion_matrix(self, results, expected, classes_qty):
        TP = 0
        FP = 0
        FN = 0
        TN = 0
        for i in range(len(results)):
            tp_idx = 0
            fp_idx = 0
            fn_idx = 0
            predictions = self.get_predictions(results[i])
            expecteds = self.get_expecteds(expected[i])
            for prediction in predictions:
                if prediction in expecteds:
                    tp_idx += 1
                    TP += 1
                else:
                    fp_idx += 1
                    FP += 1
            for expected_value in expecteds:
                if expected_value not in predictions:
                    fn_idx += 1
                    FN += 1
            TN += classes_qty - (tp_idx + fp_idx + fn_idx)
        return TN,FN,FP,TP

    def calculate_metrics(self, set, expected, metric, weights, classes_qty):
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0
        results = []
        for i in range(0, len(set)):
            results.append(self.test_forward_propagation(set[i], weights))
        true_negative, false_negative, false_positive, true_positive = self.confusion_matrix(results, expected, classes_qty)
        return metric.calculate(true_positive, true_negative, false_positive, false_negative)
