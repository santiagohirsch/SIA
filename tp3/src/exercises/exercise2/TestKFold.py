import os
import numpy as np
import pandas as pd

from Perceptron import Perceptron
from GradientDescent import GradientDescent
import MathFunctions


def linear_perceptron_test_k():

    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected = df['y'].to_numpy()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    for i in range(2, 6):
        perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.LINEAR, MathFunctions.LINEAR_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(i, training_set, expected, 2000, 0.01)
        test_errors_result = {
            'k': i,
            'test_errors': test_errors[i-1][0]
        }
        test_errors_results.append(test_errors_result)
        for j in range(len(training_errors)):
            for m in range(len(training_errors[j])):
                result = {
                    'k': i,
                    'epoch': m,
                    'training_error': training_errors[j][m][0],
                }
                results.append(result)
    results_df = pd.DataFrame(results)
    results_df.to_csv('linear_perceptron_results.csv', index=False)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv('linear_perceptron_test_errors.csv', index=False)

def non_linear_perceptron_test_k_sigmoid():

    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (0, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    for i in range(2, 6):
        perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.SIGMOID, MathFunctions.SIGMOID_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(i, training_set, expected, 2000, 0.01)
        test_errors_result = {
            'k': i,
            'beta': MathFunctions.BETA,
            'test_errors': test_errors[i-1][0]
        }
        test_errors_results.append(test_errors_result)
        for j in range(len(training_errors)):
            for m in range(len(training_errors[j])):
                result = {
                    'k': i,
                    'beta': MathFunctions.BETA,
                    'epoch': m,
                    'training_error': training_errors[j][m][0],
                }
                results.append(result)
    results_df = pd.DataFrame(results)
    results_df.to_csv('non_linear_perceptron_results_sigmoid.csv', mode='a', header=not os.path.exists('non_linear_perceptron_results_sigmoid.csv'), index=False)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv('non_linear_perceptron_test_errors_sigmoid.csv', mode='a', header=not os.path.exists('non_linear_perceptron_test_errors_sigmoid.csv'), index=False)

def non_linear_perceptron_test_k_tanh():

    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (-1, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    for i in range(2, 6):
        perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.TAN_H, MathFunctions.TAN_H_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(i, training_set, expected, 2000, 0.01)
        test_errors_result = {
            'k': i,
            'beta': MathFunctions.BETA,
            'test_errors': test_errors[i-1][0]
        }
        test_errors_results.append(test_errors_result)
        for j in range(len(training_errors)):
            for m in range(len(training_errors[j])):
                result = {
                    'k': i,
                    'beta': MathFunctions.BETA,
                    'epoch': m,
                    'training_error': training_errors[j][m][0],
                }
                results.append(result)
    results_df = pd.DataFrame(results)
    results_df.to_csv('non_linear_perceptron_results_tanh.csv', mode='a', header=not os.path.exists('non_linear_perceptron_results_tanh.csv'), index=False)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv('non_linear_perceptron_test_errors_tanh.csv', mode='a', header=not os.path.exists('non_linear_perceptron_test_errors_tanh.csv'), index=False)

   

# linear_perceptron_test_k()
non_linear_perceptron_test_k_sigmoid()
non_linear_perceptron_test_k_tanh()