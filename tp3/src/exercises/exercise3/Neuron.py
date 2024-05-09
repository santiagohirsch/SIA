import numpy as np

class Neuron:
    def __init__(self, weights, activation_function, activation_derivative ):
        self.weights = weights
        self.input = []
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.delta_w = None
        self.delta = None

    def initialize_weights(self, input_qty):
        self.weights = np.random.uniform(-1, 1, input_qty)

    def set_inputs(self, inputs):
        self.inputs = inputs

    def set_delta(self, delta):
        self.delta = delta

    def set_weights(self, weights):
        self.weights = weights

    def forward(self, inputs):
        self.inputs = inputs
        self.output = sum([self.weights[i] * self.inputs[i] for i in range(len(self.weights))]) 
        return self.output


    def calculate_output(self, inputs):
        return self.activation_function(np.dot(inputs, self.weights))   
    
    def calculate_excitement(self, inputs):
        return np.dot(inputs, self.weights)
    
    def calculate_delta(self, deltas_prev, neurons_weights):
        return np.dot(deltas_prev, neurons_weights) * self.activation_derivative(self.output)

    def update_weights(self):
        self.weights = np.array(self.weights) + np.array(self.delta_w)

    def __str__(self):
        return f'Neuron(weights={self.weights})'