import numpy as np


from MultiLayer import MultiLayer
from GradientDescent import GradientDescent
from Adam import Adam
from TrainingUtils import TrainingUtils
from font import get_characters

TAN_H = (lambda x: np.tanh(0.8 * x) )
TAN_H_DERIVATIVE = (lambda x: (1 - np.tanh(x) ** 2)* 0.8)


network = MultiLayer([49,30,20,10,5,2,5,10,20,30,49], TAN_H, TAN_H_DERIVATIVE, 0.0001, Adam())

characters = get_characters()

training_set = np.array(TrainingUtils.generate_batches(characters.copy(), 10))
training_expected = training_set.copy()

test_set = np.array(characters.copy())
test_expected = characters.copy()

network.train(training_set, training_expected, 100000, test_set, test_expected)

# test
out = network.test(test_set)
for i in range(len(test_set)):
    print("--------------------------------")
    print("Expected", test_set[i])
    print("--------------------------------")
    print("Result", out[i])