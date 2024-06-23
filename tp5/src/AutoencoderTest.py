import numpy as np


from MultiLayer import MultiLayer
from GradientDescent import GradientDescent
from Adam import Adam
from TrainingUtils import TrainingUtils
from font import get_characters, convert_to_5x7_matrix, convert_to_35_array

BETA = 0.5
TAN_H = (lambda x: np.tanh(BETA * x) )
TAN_H_DERIVATIVE = (lambda x: (1 - np.tanh(BETA * x) ** 2)* BETA)
SIGMOID = (lambda x: 1 / (1 + np.exp(-2 * BETA * x)))
SIGMOID_DERIVATIVE = (lambda x: 2 * BETA * SIGMOID(x) * (1 - SIGMOID(x)))


network = MultiLayer([35, 30, 20, 15, 10, 5, 2, 5, 10, 15, 20, 30, 35], TAN_H, TAN_H_DERIVATIVE, 0.0001, Adam())

characters = convert_to_35_array()

training_set = np.array(TrainingUtils.generate_batches(characters.copy(), 64))
training_expected = training_set.copy()

test_set = np.array(characters.copy())
test_expected = characters.copy()

network.train(training_set, training_expected, 100000, test_set, test_expected)

# test
out = network.test(test_set)[0]
for i in range(len(test_set)):
    print("--------------------------------")
    print("Expected", test_set[i])
    print("--------------------------------")
    print("Result", out[i])