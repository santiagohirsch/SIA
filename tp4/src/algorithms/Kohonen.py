import math
from neurons.KohonenNeuron import KohonenNeuron
import numpy as np

class Kohonen:
    def __init__(self, weights_qty, neurons_qty, weights_generator, similarity):
        self.weights_qty = weights_qty
        self.neurons_qty = neurons_qty
        self.weights_generator = weights_generator
        self.similarity = similarity
        self.layer = []
        for y in range(neurons_qty):
            row = []
            for x in range(neurons_qty):
                weights = weights_generator(weights_qty)
                row.append(KohonenNeuron(x, y, weights))
            self.layer.append(row)

    def get_neighbours(self, x, y, radius):
        neighbours = []

        # Redondear radius al entero más cercano
        radius_int = round(radius)

        for i in range(-radius_int, radius_int + 1):
            if x + i < 0 or x + i >= self.neurons_qty:
                continue
            for j in range(-radius_int, radius_int + 1):
                if i == 0 and j == 0:
                    continue
                if y + j < 0 or y + j >= self.neurons_qty:
                    continue
                distance = (i ** 2 + j ** 2) ** 0.5
                if distance <= radius:
                    neighbours.append(self.layer[y + j][x + i])


        return neighbours
    
    def get_winner_neuron(self, input):
        neuron = self.layer[0][0]
        neuron_similarity = self.similarity(neuron.get_weights(), input)

        for i in range(self.neurons_qty):
            for j in range(self.neurons_qty):
                current_neuron = self.layer[i][j]
                current_similarity = self.similarity(current_neuron.get_weights(), input)
                if current_similarity < neuron_similarity:
                    neuron = current_neuron
                    neuron_similarity = current_similarity

        return neuron
    
    def update_weights(self, neuron, input, learning_rate):
        weights = neuron.get_weights()
        new_weights = weights + learning_rate * (np.array(input) - np.array(weights))
        neuron.set_weights(new_weights)

    def train(self, inputs, first_learning_rate, first_radius):
        iterations = 500 * self.neurons_qty
        for i in range(iterations):
            learning_rate = first_learning_rate * math.exp(-i / iterations)
            radius = first_radius * math.exp(-i / iterations)
            if radius < 1:
                radius = 1
            for input in inputs:
                neuron = self.get_winner_neuron(input)
                neighbours = self.get_neighbours(neuron.get_x(), neuron.get_y(), radius)
                for neighbour in neighbours:
                    self.update_weights(neighbour, input, learning_rate)

        return self.layer

        