import numpy as np

"""File to encapsulate functions"""

BETA = 1

LINEAR = (lambda x: x)
LINEAR_DERIVATIVE = (lambda x: 1)

SIGMOID = (lambda x: 1 / (1 + np.exp(-2 * BETA * x)))
SIGMOID_DERIVATIVE = (lambda x: 2 * BETA * SIGMOID(x) * (1 - SIGMOID(x)))

TAN_H = (lambda x: np.tanh(x))
TAN_H_DERIVATIVE = (lambda x: 1 - np.tanh(x) ** 2)

