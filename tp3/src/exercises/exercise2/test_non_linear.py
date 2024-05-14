from math import ceil
import os as os
import pandas as pd
import numpy as np
from Perceptron import Perceptron
from GradientDescent import GradientDescent
import MathFunctions

math_functions = {
    'linear': MathFunctions.LINEAR,
    'tanh': MathFunctions.TAN_H,
    'sigmoid': MathFunctions.SIGMOID
}

math_functions_derivatives = {
    'linear': MathFunctions.LINEAR_DERIVATIVE,
    'tanh': MathFunctions.TAN_H_DERIVATIVE,
    'sigmoid': MathFunctions.SIGMOID_DERIVATIVE
}

def test_non_linear(learning_rate = 0.01, batch = 1 ,epochs = 5000, epsilon = 0.0, math_function = 'linear'):

    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']]
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (-1, 1)).tolist()
    perceptron = Perceptron(3,GradientDescent, learning_rate, math_functions.get(math_function), math_functions_derivatives.get(math_function))
    training_data, training_expected, testing_data, testing_expected = split_data(training_set.values.tolist(), expected, 0.8)
    w_min, errors = perceptron.train(training_data, training_expected, batch, epochs, epsilon)
    results = perceptron.test(testing_data, w_min)
    print("results", results)
    print("expected", testing_expected)
    # training_errors = []
    # for i in range(len(errors)):
    #     training_error = {
    #         'epoch': i,
    #         'error': errors[i][0]
    #     }
    #     training_errors.append(training_error)
    # training_errors_df = pd.DataFrame(training_errors)
    # training_errors_df.to_csv('non_linear_perceptron_tanh_training_errors.csv', index=False)


def split_data(data_set, expected, percentage):
    training_data = []
    training_expected = []
    testing_data = []
    testing_expected = []
    training_qty = ceil(len(data_set) * percentage)
    while len(training_data) < training_qty:
        i = np.random.randint(0, len(data_set) - 1)
        training_data.append(data_set[i])
        training_expected.append(expected[i])
        data_set.pop(i)
        expected.pop(i)

    testing_data = data_set
    testing_expected = expected
    return training_data, training_expected, testing_data, testing_expected

# test_non_linear()