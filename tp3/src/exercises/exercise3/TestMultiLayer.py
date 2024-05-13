import copy
from math import ceil
from matplotlib import pyplot as plt
import pandas as pd
from MultiLayer import MultiLayer
import numpy as np
from Accuracy import Accuracy
from F1 import F1
from Precision import Precision
from Recall import Recall
import random

#para digits usar 0,5, para parity 0,8 y para xor 3
TAN_H = (lambda x: np.tanh(0.8 * x) )
TAN_H_DERIVATIVE = (lambda x: (1 - np.tanh(x) ** 2)* 0.8)

def test_xor(neurons_per_layer):
    input = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    output_xor = [[-1], [1], [1], [-1]]
    network = MultiLayer(neurons_per_layer, TAN_H, TAN_H_DERIVATIVE, TAN_H, TAN_H_DERIVATIVE, 0.1)
    w_min, all_weights, all_errors, rows = network.train(input, output_xor, 4, 1500, 0.001, input, output_xor, Accuracy, 1)

    # for epoch in range(len(all_errors)):
    #     print(f"Epoch {epoch+1}: Error = {all_errors[epoch]}")

    results = network.test(input, w_min)
    for i in range(0, len(input)):
        print('input: ', input[i], 'output: ', results[i], 'expected: ', output_xor[i])


def test_parity(neurons_per_layer, expansion_factor, split_percentage):
    matrix_based_arrays = load_data()

    expected = [[1], [0], [1], [0], [1], [0], [1], [0], [1], [0]]
    network = MultiLayer(neurons_per_layer, TAN_H, TAN_H_DERIVATIVE, TAN_H, TAN_H_DERIVATIVE, 0.1)
    matrix_based_arrays, expected = expand_data(matrix_based_arrays, expected, expansion_factor)
    # matrix_based_arrays, expected, testing_data, testing_expected = split_data(matrix_based_arrays, expected, split_percentage)
    sorted_arrays = []
    sorted_expected = []
    for _ in range(0, len(matrix_based_arrays)):
        random_index = random.randint(0, len(matrix_based_arrays)-1)
        sorted_arrays.append(matrix_based_arrays[random_index])
        sorted_expected.append(expected[random_index])
        del matrix_based_arrays[random_index]
        del expected[random_index]

    matrix_based_arrays = sorted_arrays
    expected = sorted_expected
    
    print('Training data:', len(matrix_based_arrays))


    testing_data = []
    testing_expected = []

    for i in range(ceil(len(matrix_based_arrays)*(split_percentage)), len(matrix_based_arrays)):
        testing_data.append(matrix_based_arrays[i])
        testing_expected.append(expected[i])
    
    # elegi 70% para training y 30% para testing
    testing_data = add_noise(testing_data, 0.1)



    w_min, test_errors, all_errors, rows = network.train(matrix_based_arrays, expected, 1, 4000, 0.01, testing_data, testing_expected, Accuracy, 1)


    # for epoch in range(len(all_errors)):
    #     print(f"Epoch {epoch+1}: Error = {all_errors[epoch]}")
    
    results = network.test(testing_data, w_min)
    for i in range(0, len(testing_data)):
        print('input: ')
        print(np.array(testing_data[i]).reshape(7, -1))
        print('output: ', results[i], 'expected: ', testing_expected[i])


    iteraciones_all = [i * 5 for i in range(1, len(all_errors) + 1)]
    iteraciones_test = [i * 5 for i in range(1, len(test_errors) + 1)]
    plt.plot(iteraciones_all, all_errors, label='Training Errors')
    plt.plot(iteraciones_test, test_errors, label='Testing Errors')
    plt.grid()
    plt.title('Error by Epoch in Parity Function with Noise Testing ')
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.legend()
    plt.show()



def test_digits(neurons_per_layer, expansion_factor, split_percentage, noise_percentage):
    matrix_based_arrays = load_data()

    expected = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    network = MultiLayer(neurons_per_layer, TAN_H, TAN_H_DERIVATIVE, TAN_H, TAN_H_DERIVATIVE, 0.01)
    matrix_based_arrays, expected = expand_data(matrix_based_arrays, expected, expansion_factor)
    # SEPARATING DATA INTO TRAINING AND TESTING AND ADDING NOISE    
    # training_data, training_expected, testing_data, testing_expected = split_data(matrix_based_arrays, expected, split_percentage)
    # w_min, all_weights, all_errors, rows = network.train(training_data, training_expected, 1, 100000, 0.01, testing_data, testing_expected, Accuracy, 10)

    # # for epoch in range(len(all_errors)):
    # #     print(f"Epoch {epoch+1}: Error = {all_errors[epoch]}")

    
    # testing_data = add_noise(testing_data, noise_percentage)
    # results = network.test(testing_data, w_min)
    # for i in range(0, len(testing_data)):
    #     print('input: ')
    #     print(np.array(testing_data[i]).reshape(7, -1))
    #     print('output: ')
    #     for j in range(0, len(results[i])):
    #         print(round(results[i][j], 4), end=' ')
    #     print()
    #     print('expected: ', testing_expected[i])

    # TRAINING ALL THE DIGITS AND THEN TESTING ALL THE DIGITS WITH NOISE
    w_min, all_weights, all_errors, rows = network.train(matrix_based_arrays, expected, 1, 1000000, 0.01, matrix_based_arrays, expected, Accuracy, 10)

    # for epoch in range(len(all_errors)):
    #     print(f"Epoch {epoch+1}: Error = {all_errors[epoch]}")

    
    #matrix_based_arrays = add_noise(matrix_based_arrays, noise_percentage)
    matrix_based_arrays = add_noise(matrix_based_arrays, 0)

    results = network.test(matrix_based_arrays, w_min)
    for i in range(0, len(matrix_based_arrays)):
        print('input: ')
        print(np.array(matrix_based_arrays[i]).reshape(7, -1))
        print('output: ')
        for j in range(0, len(results[i])):
            print(round(results[i][j], 4), end=' ')
        print()
        print('expected: ', expected[i])
        # print('error is: ', np.sum(np.abs(np.array(results[i]) - np.array(expected[i]))))

    # TRAINING WITH AND WITHOUT NOISE
    # original_matrix_based_arrays = matrix_based_arrays
    # w_min, all_weights, all_errors = network.train(matrix_based_arrays, expected, 1, 100000, 0.01)
    # matrix_based_arrays = add_noise(matrix_based_arrays, 0.05)
    # w_min, all_weights, all_errors = network.train(matrix_based_arrays, expected, 1, 100000, 0.01)
    # matrix_based_arrays = add_noise(matrix_based_arrays, 0.05)
    # w_min, all_weights, all_errors = network.train(matrix_based_arrays, expected, 1, 100000, 0.01)
    # original_matrix_based_arrays = add_noise(original_matrix_based_arrays, 0.1)
    # results = network.test(matrix_based_arrays, w_min)
    # for i in range(0, len(matrix_based_arrays)):
    #     print('input: ')
    #     print(np.array(matrix_based_arrays[i]).reshape(7, -1))
    #     print('output: ')
    #     for j in range(0, len(results[i])):
    #         print(round(results[i][j], 4), end=' ')
    #     print()
    #     print('expected: ', expected[i])



def load_data():
    df = pd.read_csv("./TP3-ej3-digitos.txt", delimiter=' ', header=None)

    df = df.iloc[:, :-1]
    matrix_list = [df.iloc[i:i + 7, :] for i in range(0, len(df), 7)]
    matrix_based_arrays = [matrix.values.flatten() for matrix in matrix_list]
    return matrix_based_arrays

def expand_data(data_set, expected, times):
    new_data_set = []
    new_expected = []
    for i in range(0, len(data_set)):
        for _ in range(0, times):
            new_data_set.append(data_set[i])
            new_expected.append(expected[i])
    return new_data_set, new_expected

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

def add_noise(data_set, percentage):
    new_data_set = []
    for i in range(0, len(data_set)):
        numbers = 0
        new_data_set.append(data_set[i])
        for j in range(0, len(data_set[i])):
            if np.random.random() < percentage:
                numbers += 1
                new_data_set[i][j] = 1 - new_data_set[i][j]
        print(f"Added noise to {numbers} numbers")

    return new_data_set

def calculate_metric(neurons_per_layer, expansion_factor, split_percentage, metric, epochs, expected, classes_qty, split, noise):
    matrix_based_arrays = load_data()
    network = MultiLayer(neurons_per_layer, TAN_H, TAN_H_DERIVATIVE, TAN_H, TAN_H_DERIVATIVE, 0.1)
    matrix_based_arrays, expected = expand_data(matrix_based_arrays, expected, expansion_factor)
    if split:
        training_data, training_expected, testing_data, testing_expected = split_data(matrix_based_arrays, expected, split_percentage)
    else:
        training_data = copy.deepcopy(matrix_based_arrays)
        training_expected = expected
        testing_data = copy.deepcopy(matrix_based_arrays)
        testing_expected = expected
    if noise:
        testing_data = add_noise(testing_data, 0.1)

    # print("Training data")
    # for i in range(0, len(training_data)):
    #     print('input: ')
    #     print(np.array(training_data[i]).reshape(7, -1))
    #     print('expected: ', training_expected[i])

    # print("Testing data")
    # for i in range(0, len(testing_data)):
    #     print('input: ')
    #     print(np.array(testing_data[i]).reshape(7, -1))
    #     print('expected: ', testing_expected[i])

    

    w_min, _, _, rows = network.train(training_data, training_expected, 1, epochs, 0.1, testing_data, testing_expected, metric, classes_qty)

    df = pd.DataFrame(rows)
    df.to_csv(f"./F1-digits-nosplit-noise.csv", index=False)



# print('2 2 1 XOR')
# test_xor([2, 2, 1])
# print('2 2 2 2 1 XOR')
# test_xor([2, 2, 2, 2, 1])


print('35 2 1 PARITY')
test_parity([35, 2, 1], 1, 0.7)
# print('35 2 2 2 2 2 1 PARITY')
# test_parity([35, 2, 2, 2, 2, 2, 1], 1, 0.8)
# # Duplicate data set
# print('35 2 1 PARITY (DUPLICATED)')
# test_parity([35, 2, 1], 2, 0.8)
# print('35 2 2 2 2 2 1 PARITY (DUPLICATED)')
# # test_parity([35, 2, 2, 2, 2, 2, 1], 2, 0.8)

# print('35 10 10 10 DIGITS')
# test_digits([35, 10, 10], 1, 0.8, 0.1)
# print('35 10 10 10 DIGITS')
# test_digits([35, 10, 10, 10], 1, 0.8, 0.1)

# print('35 10 10 DIGITS (DUPLICATED)')
# test_digits([35, 10, 10], 2, 0.8, 0.1)
# print('35 10 10 10 DIGITS (DUPLICATED)')
# test_digits([35, 10, 10, 10], 2, 0.8, 0.1)

# calculate_metric([35, 2, 2, 2, 2, 2, 2], 1, 0.8, Accuracy, 100000, [[1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1]], 2, False, False)

# calculate_metric([35, 10, 10], 2, 0.8, F1, 1001, [
#                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], 10, True, True)