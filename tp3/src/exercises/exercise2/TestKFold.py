import os
import numpy as np
import pandas as pd

from Perceptron import Perceptron
from GradientDescent import GradientDescent
import MathFunctions

K = 5

def linear_perceptron_test_k_ordered():

    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected = df['y'].to_numpy()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.LINEAR, MathFunctions.LINEAR_DERIVATIVE)
    w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, 5000, 0.01, False)
    for j in range(len(training_errors)):
        print(f"Training errors for k={j+1}: {len(training_errors[j])}")
    # for i in range(K):
    #     test_errors_result = {
    #         'k': i+1,
    #         'test_errors': test_errors[i][0]
    #     }
    #     test_errors_results.append(test_errors_result)
    # test_errors_df = pd.DataFrame(test_errors_results)
    # test_errors_df.to_csv(f'linear_perceptron_test_errors_ordered_k{K}.csv', index=False)

def linear_perceptron_test_k_shuffled():
    
        df = pd.read_csv("TP3-ej2-conjunto.csv")
        training_set = df[['x1', 'x2', 'x3']].to_numpy()
        expected = df['y'].to_numpy()
        np.seterr(all='raise')
        results = []
        test_errors_results = []
        perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.LINEAR, MathFunctions.LINEAR_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, 5000, 0.01, True)
        for i in range(K):
            test_errors_result = {
                'k': i+1,
                'test_errors': test_errors[i][0]
            }
            test_errors_results.append(test_errors_result)
        test_errors_df = pd.DataFrame(test_errors_results)
        test_errors_df.to_csv(f'linear_perceptron_test_errors_shuffled_k{K}.csv', index=False)

def non_linear_perceptron_test_k_sigmoid_ordered():

    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (0, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.SIGMOID, MathFunctions.SIGMOID_DERIVATIVE)
    w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, 5000, 0.01, False)
    for j in range(len(training_errors)):
        print(f"Training errors for k={j+1}: {len(training_errors[j])}")
    # for i in range(K):
    #     test_errors_result = {
    #         'k': i+1,
    #         'beta': MathFunctions.BETA,
    #         'test_errors': test_errors[i][0]
    #     }
    #     test_errors_results.append(test_errors_result)
    # test_errors_df = pd.DataFrame(test_errors_results)
    # test_errors_df.to_csv(f'non_linear_perceptron_test_errors_sigmoid_ordered_k{K}.csv', index=False)

def non_linear_perceptron_test_k_sigmoid_shuffled():

    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (0, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.SIGMOID, MathFunctions.SIGMOID_DERIVATIVE)
    w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, 5000, 0.01, True)
    for i in range(K):
        test_errors_result = {
            'k': i+1,
            'beta': MathFunctions.BETA,
            'test_errors': test_errors[i][0]
        }
        test_errors_results.append(test_errors_result)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv(f'non_linear_perceptron_test_errors_sigmoid_shuffled_k{K}.csv', index=False)

def non_linear_perceptron_test_k_tanh_ordered():

    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (-1, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.TAN_H, MathFunctions.TAN_H_DERIVATIVE)
    w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, 5000, 0.01, False)
    for i in range(K):
        test_errors_result = {
            'k': i+1,
            'beta': MathFunctions.BETA,
            'test_errors': test_errors[i][0]
        }
        test_errors_results.append(test_errors_result)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv(f'non_linear_perceptron_test_errors_tanh_ordered_k{K}.csv', index=False)

def non_linear_perceptron_test_k_tanh_shuffled():
    
        df = pd.read_csv("TP3-ej2-conjunto.csv")
        training_set = df[['x1', 'x2', 'x3']].to_numpy()
        expected_set = df['y']
        min_val = min(expected_set)
        max_val = max(expected_set)
        expected = np.interp(expected_set, (min_val, max_val), (-1, 1)).tolist()
        np.seterr(all='raise')
        results = []
        test_errors_results = []
        perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.TAN_H, MathFunctions.TAN_H_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, 5000, 0.01, True)
        for i in range(K):
            test_errors_result = {
                'k': i+1,
                'beta': MathFunctions.BETA,
                'test_errors': test_errors[i][0]
            }
            test_errors_results.append(test_errors_result)
        test_errors_df = pd.DataFrame(test_errors_results)
        test_errors_df.to_csv(f'non_linear_perceptron_test_errors_tanh_shuffled_k{K}.csv', index=False)

def non_linear_perceptron_test_k_tanh_error_vs_epochs():
    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (-1, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    epoch_array = [500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 250000]
    for epoch in epoch_array:
        print("Epoch: ", epoch)
        perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.TAN_H, MathFunctions.TAN_H_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, epoch, 0, True)
        for i in range(K):
            test_errors_result = {
                'k': i+1,
                'epochs': epoch,
                'test_errors': test_errors[i][0]
            }
            test_errors_results.append(test_errors_result)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv(f'non_linear_perceptron_tanh_test_errors_vs_epochs_k{K}.csv', index=False)

def non_linear_perceptron_test_k_sigmoid_error_vs_epochs():
    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (0, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    epoch_array = [500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 250000]
    for epoch in epoch_array:
        print("Epoch: ", epoch)
        perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.SIGMOID, MathFunctions.SIGMOID_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, epoch, 0, True)
        for i in range(K):
            test_errors_result = {
                'k': i+1,
                'epochs': epoch,
                'test_errors': test_errors[i][0]
            }
            test_errors_results.append(test_errors_result)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv(f'non_linear_perceptron_sigmoid_test_errors_vs_epochs_k{K}.csv', index=False)

def non_linear_perceptron_test_k_tanh_error_vs_beta():
    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (-1, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    beta_array = [1, 2, 3, 4, 5]
    for beta in beta_array:
        print("Beta: ", beta)
        MathFunctions.BETA = beta
        perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.TAN_H, MathFunctions.TAN_H_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, 5000, 0, True)
        for i in range(K):
            test_errors_result = {
                'k': i+1,
                'beta': beta,
                'test_errors': test_errors[i][0]
            }
            test_errors_results.append(test_errors_result)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv(f'non_linear_perceptron_tanh_test_errors_vs_beta.csv', index=False)

def non_linear_perceptron_test_k_sigmoid_error_vs_beta():
    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (0, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    beta_array = [1, 2, 3, 4, 5]
    for beta in beta_array:
        print("Beta: ", beta)
        MathFunctions.BETA = beta
        perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.SIGMOID, MathFunctions.SIGMOID_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, 100000, 0, True)
        for i in range(K):
            test_errors_result = {
                'k': i+1,
                'beta': beta,
                'test_errors': test_errors[i][0]
            }
            test_errors_results.append(test_errors_result)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv(f'non_linear_perceptron_sigmoid_test_errors_vs_beta.csv', index=False)

def non_linear_perceptron_test_k_sigmoid_error_vs_learning():
    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (0, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    learning_array = [0.001, 0.005, 0.01, 0.05, 0.1]
    for learning in learning_array:
        print("Learning: ", learning)
        perceptron = Perceptron(3, GradientDescent, learning, MathFunctions.SIGMOID, MathFunctions.SIGMOID_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, 100000, 0, True)
        for i in range(K):
            test_errors_result = {
                'k': i+1,
                'learning': learning,
                'test_errors': test_errors[i][0]
            }
            test_errors_results.append(test_errors_result)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv(f'non_linear_perceptron_sigmoid_test_errors_vs_learning.csv', index=False)

def non_linear_perceptron_test_k_sigmoid_error_vs_batch():
    df = pd.read_csv("TP3-ej2-conjunto.csv")
    training_set = df[['x1', 'x2', 'x3']].to_numpy()
    expected_set = df['y']
    min_val = min(expected_set)
    max_val = max(expected_set)
    expected = np.interp(expected_set, (min_val, max_val), (0, 1)).tolist()
    np.seterr(all='raise')
    results = []
    test_errors_results = []
    batch_array = [1, len(training_set) -1]
    for batch in batch_array:
        print("Batch: ", batch)
        perceptron = Perceptron(3, GradientDescent, 0.01, MathFunctions.SIGMOID, MathFunctions.SIGMOID_DERIVATIVE)
        w_min, training_errors, test_errors = perceptron.k_test(K, training_set, expected, 100000, 0, True, batch)
        for i in range(K):
            test_errors_result = {
                'k': i+1,
                'batch': batch,
                'test_errors': test_errors[i][0]
            }
            test_errors_results.append(test_errors_result)
    test_errors_df = pd.DataFrame(test_errors_results)
    test_errors_df.to_csv(f'non_linear_perceptron_sigmoid_test_errors_vs_batch.csv', index=False)
   
# print("Linear Perceptron Test K Ordered")
# linear_perceptron_test_k_ordered()

# # print("Linear Perceptron Test K Shuffled")
# # linear_perceptron_test_k_shuffled()

# print("Non Linear Perceptron Test K Sigmoid Ordered")
# non_linear_perceptron_test_k_sigmoid_ordered()

# print("Non Linear Perceptron Test K Sigmoid Shuffled")
# non_linear_perceptron_test_k_sigmoid_shuffled()

# print("Non Linear Perceptron Test K Tanh Ordered")
# non_linear_perceptron_test_k_tanh_ordered()

# print("Non Linear Perceptron Test K Tanh Shuffled")
# non_linear_perceptron_test_k_tanh_shuffled()

# print("Non Linear Perceptron Test K Tanh Error vs Epochs")
# non_linear_perceptron_test_k_tanh_error_vs_epochs()

# print("Non Linear Perceptron Test K Sigmoid Error vs Epochs")
# non_linear_perceptron_test_k_sigmoid_error_vs_epochs()

# print("Non Linear Perceptron Test K Tanh Error vs Beta")
# non_linear_perceptron_test_k_tanh_error_vs_beta()

# print("Non Linear Perceptron Test K Sigmoid Error vs Beta")
# non_linear_perceptron_test_k_sigmoid_error_vs_beta()

# print("Non Linear Perceptron Test K Sigmoid Error vs Learning")
# non_linear_perceptron_test_k_sigmoid_error_vs_learning()

print("Non Linear Perceptron Test K Sigmoid Error vs Batch")
non_linear_perceptron_test_k_sigmoid_error_vs_batch()