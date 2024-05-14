import json
import sys
import random
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt


input = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
output_and = [-1, -1, -1, 1]
output_xor = [-1, 1, 1, -1]
ws = []

def initialize_weights():
    w = []
    for _ in range(0,3):
        w.append(random.uniform(-1, 1))
    return w

def compute_excitement(weights, values):
    return weights[0] + weights[1] * values[0] + weights[2] * values[1]

def compute_activation(excitement):
    return 1 if excitement > 0 else -1

def compute_error(weights, output):
    error_count = 0
    for i in range(0,len(input)):
        excitement = compute_excitement(weights, input[i])
        activation = compute_activation(excitement)
        error_count += 1 if activation != output[i] else 0
    return error_count/len(input)


def simple_percepton(learning_rate = 0.1, limit = 200):
    i = 0
    w = initialize_weights()
    ws.append(w)
    error = None
    min_error = sys.maxsize
    w_min = None
    errors = []
    while (min_error > 0 and i < limit):
        m = random.randint(0, len(input) - 1)
        excitement = compute_excitement(w, input[m])
        activation = compute_activation(excitement)
        deltas = np.dot([1] + input[m], learning_rate * (output_and[m] - activation))
        
        w = w + deltas
        ws.append(w)
        error = compute_error(w, output_and)
        errors.append(error)
        if error < min_error:
            min_error = error
            w_min = w
        i += 1
    return w_min,errors


w_min, errors = simple_percepton(0.1, 200)

# # Extract the weights for plotting the decision boundary
# w0 = w_min[0]
# w1 = w_min[1]
# w2 = w_min[2]

# # Define the x and y values for the decision boundary line
# x = np.linspace(-2, 2, 100)
# y = (-w0 - w1 * x) / w2

# # Plot the decision boundary line
# plt.plot(x, y, label='Decision Boundary')

# # Plot the input points
# for i in range(len(input)):
#     if output_and[i] == 1:
#         plt.scatter(input[i][0], input[i][1], color='blue', label='Class 1')
#     else:
#         plt.scatter(input[i][0], input[i][1], color='red', label='Class -1')

# plt.xlabel('Input 1')
# plt.ylabel('Input 2')
# plt.title('Perceptron Decision Boundary')
# plt.legend()
# plt.grid()
# plt.show()


# Plot the error rate
# plt.plot(errors)
# plt.xlabel('Iterations')
# plt.ylabel('Error Rate')
# plt.title('Error Rate vs Iterations')
# plt.grid()
# plt.show()