import json
import sys
import random
import numpy as np

input = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
output_and = [-1, -1, -1, 1]
output_xor = [1, 1, -1, -1]
ws = []

def initialize_weights():
    w = []
    for i in range(len(input)):

        w.append(input[i][random.randint(0, 1)])
    return w

def compute_excitement(weights, values):
    return weights[0] + weights[1] * values[0] + weights[2] * values[1]

def compute_activation(excitement):
    return 1 if excitement > 0 else -1

def compute_error(weights, output):
    total_error = 0
    for i in range(len(input)):
        excitement = compute_excitement(weights, [1] + input[i])
        activation = compute_activation(excitement)
        total_error += (output[i] - activation) ** 2
    return total_error


def simple_percepton():
    learning_rate = 0.1
    i = 0
    w = initialize_weights()
    ws.append(w)
    limit = 1000000
    error = None
    min_error = sys.maxsize
    w_min = None

    while (min_error > 0 and i < limit):
        m = random.randint(0, len(input) - 1)
        excitement = compute_excitement(w, input[m])
        print('excitement', excitement)
        activation = compute_activation(excitement)
        print('activation', activation)
        deltas = np.dot([1] + input[m], learning_rate * (output_and[m] - activation))
        print('delta', deltas)
        w = np.add(w, deltas)
        ws.append(w)
        error = compute_error(w, output_and)
        if error < min_error:
            min_error = error
            w_min = w
        i += 1
    return w_min


print(simple_percepton())