import numpy as np

class Oja:
    def __init__(self, input_qty, weight_generator):
        self.input_qty = input_qty
        self.weights = weight_generator(input_qty)
        
    def activation(self, input):
        return np.dot(input, self.weights)
    
    def update_weights(self, input, learning_rate):
        self.weights += learning_rate * (input * self.activation(input) - self.activation(input)**2 * self.weights)

    def train(self, inputs, learning_rate, epochs):
        for _ in range(epochs):
            for input in inputs:
                self.update_weights(input, learning_rate)

        return self.weights

        


    