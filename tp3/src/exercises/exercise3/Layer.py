import random
import numpy as np
import Neuron

class Layer:
    def __init__(self,neurons_qty,weights, activation_function, activation_derivative):
        self.neurons_qty = neurons_qty
        neurons = []
        for i in range(neurons_qty):
            neurons.append(Neuron(weights, activation_function, activation_derivative))
        self.neurons = neurons
        self.weights = weights
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative

    def initialize_weights(self, input_qty):
        self.weights = np.random.uniform(-1, 1, input_qty)
        for neuron in self.neurons:
            neuron.initialize_weights(input_qty)
            neuron.delta_w = np.zeros(input_qty)

    def forward(self, inputs):
        out = []
        for neuron in self.neurons:
            neuron.set_inputs([1] + inputs) #agrego el bias
            out.append(neuron.calculate_output())
        return out
    
    def update_neuron_weights(self):
        for neuron in self.neurons:
            neuron.update_weights()
            neuron.delta_w = np.zeros(len(neuron.weights))
            
    def calculate_deltas(self, deltas_prev, neurons_weights):
        deltas = []
        for i in range(self.neurons_qty):
            deltas.append(self.neurons[i].calculate_delta(deltas_prev, neurons_weights[i]))
        return deltas