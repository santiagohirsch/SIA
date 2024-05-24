import csv
from matplotlib import pyplot as plt
import numpy as np
from algorithms.Kohonen import Kohonen
from similarity.Euclidean import Euclidean

def kohonen():
    archivo_csv = '../data/europe.csv'

    HEADER = []
    DATA = []
    COUNTRIES = []

    with open(archivo_csv, 'r') as f:
        reader = csv.reader(f)
        HEADER = next(reader)
        for row in reader:
            COUNTRIES.append(row[0])
            DATA.append(row[1:])

    DATA = np.array(DATA).astype(float)
    DATA = DATA / np.linalg.norm(DATA, axis=1)[:, np.newaxis]

    weights_qty = len(DATA[0])
    neurons_qty = 10
    learning_rate = 0.1
    radius = 5

    kohonen = Kohonen(weights_qty, neurons_qty, lambda x: np.random.rand(x), Euclidean.similarity)
    kohonen.train(DATA, learning_rate, radius)
    heat_map(kohonen, DATA, COUNTRIES)

def u_matrix(network):
    u_matrix = np.zeros((network.neurons_qty, network.neurons_qty))
    for i in range(network.neurons_qty):
        for j in range(network.neurons_qty):
            neuron = network.layer[i][j]
            neighbours = network.get_neighbours(j, i, 1)
            total_distance = 0
            for neighbour in neighbours:
                total_distance += network.similarity(neighbour.get_weights(), neuron.get_weights())
            u_matrix[i][j] = total_distance / len(neighbours)
    return u_matrix

def heat_map(network, input, countries):
    matrix = u_matrix(network)
    plt.figure(figsize=(10, 10))
    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.title('U-Matrix')
    plt.colorbar()
    plt.show()

kohonen()