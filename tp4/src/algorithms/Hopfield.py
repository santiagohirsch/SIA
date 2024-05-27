import numpy as np
from algorithms.HopfieldNeuron import HopfieldNeuron

class Hopfield:
    def __init__(self,  patterns, input_state):
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
        matrix = []
        for neuron in self.neurons:
            matrix.append(neuron.get_weights())
        return matrix
    
    def get_states(self):  
        states = []
        for neuron in self.neurons:
            states.append(neuron.get_state())
        return states
    

    def energy(self,weights,states):
        energy = 0
        for i in range(len(weights[0])):
            for j in range(len(weights[0])):
                if i < j:
                    energy += weights[i][j] * states[i] * states[j]
        return -1 * energy

    def train(self, epochs: int):
        energy_array = []
        prev_states = self.get_states()
        prev_prev_states = []
        while(epochs > 0):
            epochs -= 1
            print("Epochs :",epochs)
            for i, neuron in enumerate(self.neurons):
                net = 0
                for j, other_neuron in enumerate(self.neurons):
                    if i == j:
                        continue
                    net += other_neuron.get_state() * neuron.get_weights()[j]
                if net > 0:
                    neuron.set_state(1)
                else: 
                    if net < 0:
                        neuron.set_state(-1)
                    else :
                        print("Error: state was 0")
            
            if np.array_equal(prev_states, self.get_states()) and prev_prev_states == prev_states:
                return self.get_states()
            prev_prev_states = prev_states
            prev_states = self.get_states()
            energy_array.append(self.energy(self.get_weights_matrix(), self.get_states()))
        return self.get_states()
    
