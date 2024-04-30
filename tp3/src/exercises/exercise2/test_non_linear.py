import os as os
import pandas as pd
import numpy as np
from Perceptron import Perceptron
from GradientDescent import GradientDescent
import MathFunctions



def test_non_linear():

    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y'].to_numpy()
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (-1, 1)).tolist()
    perceptron = Perceptron(3,GradientDescent, 0.1,MathFunctions.LINEAR, MathFunctions.LINEAR_DERIVATIVE)
    w_min, errors = perceptron.train(training_set, expected, 1, 30000, 2.0)
    results = perceptron.test(training_set, w_min)

    print('expected: ', expected)
    print('results: ', results)


test_non_linear()