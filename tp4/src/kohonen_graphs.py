import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
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

    # DATA = np.array(DATA).astype(float)
    # DATA = DATA / np.linalg.norm(DATA, axis=1)[:, np.newaxis]

    df = pd.DataFrame(DATA).astype(float)
    df = df.apply(lambda x: (x - np.mean(x)) / np.std(x), axis=0)
    # df = df.transpose()

    weights_qty = len(DATA[0])
    neurons_qty = 3
    learning_rate = 0.1
    radius = 3
    # random_country = np.random.choice(len(df.values.tolist()) - 1)
    # print(random_country)
    # print(COUNTRIES[random_country])
    # print(df.values.tolist()[random_country])
    # kohonen = Kohonen(weights_qty, neurons_qty, lambda x: np.random.uniform(0, 1, x), Euclidean.similarity)
    kohonen = Kohonen(weights_qty, neurons_qty, lambda x: df.values.tolist()[np.random.choice(len(df.values.tolist()) - 1)], Euclidean.similarity)
    
    # layer = kohonen.train(df.values.tolist(), learning_rate, radius)
    with_color = True
    # plot_complete_heatmap(kohonen, df.values.tolist(), COUNTRIES, not with_color)
    # plot_u_matrix_by_var(kohonen, HEADER, not with_color)
    # # kohonen_4neurons = Kohonen(weights_qty, 4, lambda x: np.random.uniform(0, 1, x), Euclidean.similarity)
    kohonen_4neurons = Kohonen(weights_qty, 4, lambda x: df.values.tolist()[np.random.choice(len(df.values.tolist()) - 1)], Euclidean.similarity)
    layer = kohonen_4neurons.train(df.values.tolist(), 0.1, 4)
    plot_complete_heatmap(kohonen_4neurons, df.values.tolist(), COUNTRIES, with_color)
    # plot_u_matrix_by_var(kohonen_4neurons, HEADER, with_color)
    plot_heatmap_by_var(kohonen_4neurons, HEADER)
    

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

def u_matrix_by_var(network, var, euclidean=False):
    u_matrix = np.zeros((network.neurons_qty, network.neurons_qty))
    for i in range(network.neurons_qty):
        for j in range(network.neurons_qty):
            neuron = network.layer[i][j]
            neighbours = network.get_neighbours(j, i, 1)
            distances = []
            for neighbour in neighbours:
                if euclidean:
                    distances.append(network.similarity(neighbour.get_weights()[var], neuron.get_weights()[var]))
                else:
                    distances.append(abs(neighbour.get_weights()[var] - neuron.get_weights()[var]))
            u_matrix[i][j] = np.mean(distances)
    return u_matrix

# def plot_u_matrix(network):
#     matrix = u_matrix(network)
#     plt.figure(figsize=(10, 10))
#     plt.imshow(matrix, cmap='gray', interpolation='nearest')
#     plt.title('U-Matrix')
#     plt.colorbar()
    
#     # Add annotations to each cell
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             plt.text(j, i, round(matrix[i][j], 2), ha='center', va='center', color='red')
    
#     plt.show()

def plot_u_matrix_by_var(network, header, color):
    if color:
        cmap = 'hot'
        title = 'Average Value per Neuron - '
        text_color = 'lime'
    else:
        cmap = 'gray'
        title = 'U-Matrix For '
        text_color = 'red'
    for idx, name in enumerate(header[1:]):
        matrix = u_matrix_by_var(network, idx)
        plt.figure(figsize=(10, 10))
        plt.imshow(matrix, cmap, interpolation='nearest')
        plt.title(title + name)
        plt.colorbar()
        
        if not color:
            # Add annotations to each cell
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    plt.text(j, i, round(matrix[i][j], 2), ha='center', va='center', color=text_color)
        
        plt.show()

def plot_heatmap_by_var(network, header):
    for idx, name in enumerate(header[1:]):
        heatmap = np.zeros((network.neurons_qty, network.neurons_qty))
        for i in range(network.neurons_qty):
            for j in range(network.neurons_qty):
                neuron = network.layer[i][j]
                heatmap[i][j] = neuron.get_weights()[idx]
        plt.figure(figsize=(10, 10))
        plt.imshow(heatmap, cmap='hot', interpolation='nearest')
        plt.title('Heatmap for ' + name)
        plt.colorbar()
        plt.show()

def plot_complete_heatmap(network, input, countries, color):
    if color:
        cmap = 'hot'
        text_color = 'lime'
    else:
        cmap = 'gray'
        text_color = 'red'
    winner_neurons = [network.neurons_qty * [0] for _ in range(network.neurons_qty)]
    countries_map = [network.neurons_qty * [''] for _ in range(network.neurons_qty)]
    for idx, row in enumerate(input):
        neuron = network.get_winner_neuron(row)
        winner_neurons[neuron.get_y()][neuron.get_x()] += 1
        countries_map[neuron.get_y()][neuron.get_x()] += countries[idx] + '\n'
    
    plt.figure(figsize=(10, 10))
    plt.imshow(winner_neurons, cmap, interpolation='nearest')
    plt.title('Complete Heatmap')
    plt.colorbar()

    # Add annotations to each cell
    for i in range(len(winner_neurons)):
        for j in range(len(winner_neurons[i])):
            plt.text(j, i, countries_map[i][j], ha='center', va='center', color=text_color)
            
    plt.show()

kohonen()