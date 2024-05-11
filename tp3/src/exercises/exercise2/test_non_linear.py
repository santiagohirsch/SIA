from math import ceil
import os as os
import pandas as pd
import numpy as np
from Perceptron import Perceptron
from GradientDescent import GradientDescent
import MathFunctions



def test_non_linear():

    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']]
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (0, 1)).tolist()
    perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.SIGMOID, MathFunctions.SIGMOID_DERIVATIVE)
    training_data, training_expected, testing_data, testing_expected = split_data(training_set.values.tolist(), expected, 0.8)
    w_min, errors = perceptron.train(training_data, training_expected, 1, 200000, 0.1)
    results = perceptron.test(testing_data, w_min)

    print('expected: ', testing_expected)
    print('results: ', results)


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

test_non_linear()