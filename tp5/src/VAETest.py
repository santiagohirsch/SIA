import numpy as np

from Autoencoder import Autoencoder
from MultiLayer import MultiLayer
from Adam import Adam
from TrainingUtils import TrainingUtils
from font import get_characters

TAN_H = (lambda x: np.tanh(0.8 * x) )
TAN_H_DERIVATIVE = (lambda x: (1 - np.tanh(x) ** 2)* 0.8)

learning_rate = 0.0001

encoder = MultiLayer([49,30,20,10,4], TAN_H, TAN_H_DERIVATIVE, learning_rate, Adam)
decoder = MultiLayer([2,10,20,30,49], TAN_H, TAN_H_DERIVATIVE, learning_rate, Adam)

autoencoder = Autoencoder(encoder, decoder)

characters = get_characters()
test_set = np.array(characters.copy())

autoencoder.train(test_set, 100000)

# test
out = autoencoder.test(test_set)

for i in range(len(test_set)):
    print("--------------------------------")
    print("Expected", test_set[i])
    print("--------------------------------")
    print("Result", out[i])
