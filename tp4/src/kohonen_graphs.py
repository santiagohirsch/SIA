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
    neurons_qty = 3
    learning_rate = 0.1
    radius = 3

    kohonen = Kohonen(weights_qty, neurons_qty, lambda x: np.random.uniform(0, 1), Euclidean.similarity)
    kohonen.train(DATA, learning_rate, radius)
    # plot_u_matrix(kohonen)
    plot_u_matrix_by_var(kohonen, HEADER)
    # plot_complete_heatmap(kohonen, DATA, COUNTRIES)

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

def u_matrix_by_var(network, var):
    u_matrix = np.zeros((network.neurons_qty, network.neurons_qty))
    for i in range(network.neurons_qty):
        for j in range(network.neurons_qty):
            neuron = network.layer[i][j]
            neighbours = network.get_neighbours(j, i, 1)
            distances = []
            for neighbour in neighbours:
                distances.append(abs(neighbour.get_weights()[var] - neuron.get_weights()[var]))
            u_matrix[i][j] = np.mean(distances)
    return u_matrix

def plot_u_matrix(network):
    matrix = u_matrix(network)
    plt.figure(figsize=(10, 10))
    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.title('U-Matrix')
    plt.colorbar()
    
    # Add annotations to each cell
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            plt.text(j, i, round(matrix[i][j], 2), ha='center', va='center', color='blue')
    
    plt.show()

def plot_u_matrix_by_var(network, header):
    for idx, name in enumerate(header[1:]):
        matrix = u_matrix_by_var(network, idx)
        plt.figure(figsize=(10, 10))
        plt.imshow(matrix, cmap='gray', interpolation='nearest')
        plt.title('U-Matrix ' + name)
        plt.colorbar()
        
        # Add annotations to each cell
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                plt.text(j, i, round(matrix[i][j], 2), ha='center', va='center', color='red')
        
        plt.show()

def plot_complete_heatmap(network, input, countries):
    winner_neurons = [network.neurons_qty * [0] for _ in range(network.neurons_qty)]
    countries_map = [network.neurons_qty * [''] for _ in range(network.neurons_qty)]
    for idx, row in enumerate(input):
        neuron = network.get_winner_neuron(row)
        winner_neurons[neuron.get_y()][neuron.get_x()] += 1
        countries_map[neuron.get_y()][neuron.get_x()] += countries[idx] + '\n'
    
    plt.figure(figsize=(10, 10))
    plt.imshow(winner_neurons, cmap='gray', interpolation='nearest')
    plt.title('Heatmap')
    plt.colorbar()

    # Add annotations to each cell
    for i in range(len(winner_neurons)):
        for j in range(len(winner_neurons[i])):
            plt.text(j, i, countries_map[i][j], ha='center', va='center', color='red')
            
    plt.show()

kohonen()