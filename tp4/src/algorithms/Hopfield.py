import numpy as np
import src.algorithms.HopfieldNeuron as HopfieldNeuron

class Hopfield:
    def __init__(self,  patterns: list[list[int]], input_state: list[int]):
        self.patterns = patterns
        self.neurons = []
        for i, state in enumerate(input_state):
            self.neurons.append(HopfieldNeuron(state, self.calculate_weights(i)))


    def calculate_weights(self, index: int):
        n = len(self.patterns[0])
        p = len(self.patterns)
        weights = np.zeros(n)
        for i in range(n):
            if i == index:
                weights[i] = 0
                continue
            for mu in range(p):
                weights[i] += self.patterns[mu][index] * self.patterns[mu][i]
            weights[i] = (1 / n) * weights[i]
        return weights
            
    def get_weights_matrix(self):
        matrix = np.zeros(self.n)
        for neuron in self.neurons:
            matrix.append(neuron.get_weights())
        return matrix
    
    def get_states(self):  
        states = []
        for neuron in self.neurons:
            states.append(neuron.get_state())
        return states