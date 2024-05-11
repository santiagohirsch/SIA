from math import ceil
import numpy as np
import pandas as pd
from Perceptron import Perceptron
from GradientDescent import GradientDescent
import MathFunctions

def TestLinear():
    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']]
    expected = df['y']
    
    perceptron = Perceptron(3,GradientDescent, 0.01, MathFunctions.LINEAR, MathFunctions.LINEAR_DERIVATIVE)
    # training_data, training_expected, testing_data, testing_expected = split_data(training_set.values.tolist(), expected.values.tolist(), 0.8)
    w_min, errors = perceptron.train(training_set.values.tolist(), expected.values.tolist(), 1, 20000, 2.0)
    # results = perceptron.test(testing_data, w_min)
    # mse = 0
    # for i in range(0, len(results)):
    #     mse += (results[i] - testing_expected[i])**2
    # mse = mse / len(results)
    
    # print('expected: ', testing_expected)
    # print('results: ', results)
    # print('mse: ', mse)

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

TestLinear()