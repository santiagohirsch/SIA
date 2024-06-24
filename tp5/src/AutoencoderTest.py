from math import ceil
import random
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import plotly.graph_objects as go

from MultiLayer import MultiLayer
from GradientDescent import GradientDescent
from Adam import Adam
from TrainingUtils import TrainingUtils
from font import get_characters, convert_to_5x7_matrix, convert_to_35_array

BETA = 0.5
TAN_H = (lambda x: np.tanh(BETA * x) )
TAN_H_DERIVATIVE = (lambda x: (1 - np.tanh(BETA * x) ** 2)* BETA)
SIGMOID = (lambda x: 1 / (1 + np.exp(-2 * BETA * x)))
SIGMOID_DERIVATIVE = (lambda x: 2 * BETA * SIGMOID(x) * (1 - SIGMOID(x)))

def split_data_by_count(characters, train_count):

    random.shuffle(characters)  # Mezcla aleatoriamente los caracteres

    train_set = characters[:train_count]
    test_set = characters[train_count:]

    return train_set, test_set

def test_autoencoder():
    # for i in range(35):
    #     print("i: ", i)
    #     print("random: ", random.random())  
    #     print('-'*50)
    network = MultiLayer([35, 30, 20, 15, 10, 5, 2, 5, 10, 15, 20, 30, 35], TAN_H, TAN_H_DERIVATIVE, 0.0001, Adam())

    characters = convert_to_35_array()

    # training_set, training_expected, test_set, test_expected = split_data(characters, characters.copy(), 0.8)

    training_set = np.array(TrainingUtils.generate_batches(characters.copy(), 32))
    training_expected = training_set.copy()

    test_set = np.array(characters.copy())
    test_expected = characters.copy()

    network.train(training_set, training_expected, 100000, test_set, test_expected)

    # test
    expected_set = test_set.copy()
    for i in range(len(test_set)):
        test_set[i] = TrainingUtils.add_noise(test_set[i], 0.1)
    out = network.test(test_set)[0]
    
    for i in range(len(test_set)):
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))

        print("--------------------------------")
        print("Input")
        axs[0].imshow(test_set[i].reshape(7, 5), cmap='gray_r', interpolation='nearest')
        axs[0].set_title("Input")
        axs[0].axis('off')

        print("--------------------------------")
        print("Output")
        axs[1].imshow(out[i].reshape(7, 5), cmap='gray_r', interpolation='nearest')
        axs[1].set_title("Output")
        axs[1].axis('off')

        print("--------------------------------")
        print("Expected")
        axs[2].imshow(expected_set[i].reshape(7, 5), cmap='gray_r', interpolation='nearest')
        axs[2].set_title("Expected")
        axs[2].axis('off')

        plt.show()
    return network

def save_latent_space_to_csv(network, csv_path):
    middle_layer = network.layers[len(network.layers) // 2]
    latent_space = middle_layer.output
    characters = ['`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'DEL'
                  ]

    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(latent_space)

    pca_df = pd.DataFrame(pca_result, columns=['PCA 1', 'PCA 2'])
    pca_df['Character'] = characters

    # Save the DataFrame to a CSV file
    pca_df.to_csv(csv_path, index=False)

def plot_latent_space_from_csv(csv_path):
    # Load the data from the CSV file
    pca_df = pd.read_csv(csv_path)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=pca_df['PCA 1'],
        y=pca_df['PCA 2'],
        mode='markers',
        marker=dict(color='Blue', size=20),
        text=pca_df['Character'],
        name='PCA Plot'
    ))

    # Add annotations for character labels
    for i, row in pca_df.iterrows():
        fig.add_annotation(
            x=row['PCA 1'],
            y=row['PCA 2'],
            text=row['Character'],
            showarrow=False,
            font=dict(size=20, color='black')
        )

    # Customize layout
    fig.update_layout(
        title='Scatter plot of latent space',
        xaxis=dict(title='Dimension 1'),
        yaxis=dict(title='Dimension 2'),
    )

    # Show the plot
    fig.show()

# csv_path = 'latent_space.csv'
# save_latent_space_to_csv(test_autoencoder(), csv_path)
# plot_latent_space_from_csv(csv_path)
test_autoencoder()