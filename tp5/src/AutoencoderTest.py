import colorsys
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

def test_autoencoder(pixel_errors = False):
    # for i in range(35):
    #     print("i: ", i)
    #     print("random: ", random.random())  
    #     print('-'*50)
    network = MultiLayer([35, 30, 20, 15, 10, 5, 2, 5, 10, 15, 20, 30, 35], TAN_H, TAN_H_DERIVATIVE, 0.01, Adam())

    characters = convert_to_35_array()

    # training_set, training_expected, test_set, test_expected = split_data(characters, characters.copy(), 0.8)

    training_set = np.array(TrainingUtils.generate_batches(characters.copy(), 32))
    training_expected = training_set.copy()
    # training_noisy = np.array([TrainingUtils.add_noise(x, 0.1) for x in training_set])

    test_set = np.array(characters.copy())
    test_expected = characters.copy()

    _, pixel_errors = network.train(training_set, training_expected, 100000, test_set, test_expected)

    if pixel_errors:
        data = []
        for i, error in enumerate(pixel_errors):
            epoch = (i + 1) * 1000  
            data.append({'epoca': epoch, 'error': error})

        # Crear el DataFrame a partir de la lista de datos
        df = pd.DataFrame(data)


        # Escribir el DataFrame a un archivo CSV
        csv_path = 'pixel_errors.csv'
        df.to_csv(csv_path, index=False)




    # test
    expected_set = test_set.copy()
    for i in range(len(test_set)):
        test_set[i] = TrainingUtils.add_noise(test_set[i], 0.15)
    out = network.test(test_set)[0]

    errors = 0
    for i in range(len(test_set)):
        distinct = 0
        print("Out", out[i]), print("Expected", expected_set[i])
        for j in range(len(test_set)):
            if (out[i][j] > 0 and expected_set[i][j] < 0) or (out[i][j] < 0 and expected_set[i][j] > 0):
                distinct += 1
        print("Distinct: ", distinct)
        if distinct > 2:
            errors += 1

    print("Errors: ", errors)
    
    # for i in range(len(test_set)):
    #     fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    #     print("--------------------------------")
    #     print("Input")
    #     axs[0].imshow(test_set[i].reshape(7, 5), cmap='gray_r', interpolation='nearest')
    #     axs[0].set_title("Input")
    #     axs[0].axis('off')

    #     print("--------------------------------")
    #     print("Output")
    #     axs[1].imshow(out[i].reshape(7, 5), cmap='gray_r', interpolation='nearest')
    #     axs[1].set_title("Output")
    #     axs[1].axis('off')

    #     print("--------------------------------")
    #     print("Expected")
    #     axs[2].imshow(expected_set[i].reshape(7, 5), cmap='gray_r', interpolation='nearest')
    #     axs[2].set_title("Expected")
    #     axs[2].axis('off')

    #     plt.show()
    return network

def plot_error_vs_epoch(csv_path):
    # Cargar datos desde el archivo CSV
    df = pd.read_csv(csv_path)
    
    # Obtener los valores de época y error
    epochs = df['epoca']
    errors = df['error']
    
    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(epochs, errors, linestyle='-', color='b', label='Error vs. Época')
    
    # Etiquetas y título
    plt.xlabel('Época')
    plt.ylabel('Error')
    plt.title('Error en función de la Época')
    
    # Mostrar la leyenda y grid si es necesario
    plt.legend()
    plt.grid(True)
    
    # Mostrar el gráfico
    plt.show()

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

def generate_distinct_colors(n):
    colors = []
    for i in range(n):
        hue = i / n
        saturation = 0.7  # Fixed saturation for vibrant colors
        value = 0.9       # Fixed value for bright colors
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        hex_color = f'#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}'
        colors.append(hex_color)
    return colors

def plot_latent_space_from_csv(csv_path):
    # Load the data from the CSV file
    pca_df = pd.read_csv(csv_path)

    # Generate 32 distinct colors
    unique_characters = pca_df['Character'].unique()
    if len(unique_characters) > 32:
        raise ValueError("More than 32 unique characters, cannot generate enough distinct colors.")
    
    distinct_colors = generate_distinct_colors(32)
    colors = {char: distinct_colors[i] for i, char in enumerate(unique_characters)}

    fig = go.Figure()

    # Add scatter plot trace
    fig.add_trace(go.Scatter(
        x=pca_df['PCA 1'],
        y=pca_df['PCA 2'],
        mode='markers',
        marker=dict(size=20, color=[colors[char] for char in pca_df['Character']]),
        name='PCA Plot'
    ))

    # Calculate positions for annotations outside the main scatter area
    x_max = pca_df['PCA 1'].max()
    y_min = pca_df['PCA 2'].min()
    y_max = pca_df['PCA 2'].max()

    # Determine the spacing for the list of labels on the right
    y_spacing = (y_max - y_min) / len(unique_characters)
    y_start = y_max

    # Add annotations for character labels at the side of the plot
    for i, char in enumerate(unique_characters):
        # Calculate the y position for each label
        y_pos = y_start - i * y_spacing

        # Add a colored circle as a marker
        fig.add_trace(go.Scatter(
            x=[x_max + (x_max * 0.1)],  # Shift annotations to the right of the plot
            y=[y_pos],
            mode='markers',
            marker=dict(size=20, color=colors[char]),
            showlegend=False
        ))

        # Add the character label next to the colored circle
        fig.add_annotation(
            x=x_max + (x_max * 0.15),  # Position label to the right of the circle
            y=y_pos,
            text=char,
            showarrow=False,
            font=dict(size=15, color='black')
        )

    # Customize layout
    fig.update_layout(
        title='Scatter plot of latent space',
        xaxis=dict(title='Dimension 1'),
        yaxis=dict(title='Dimension 2'),
        margin=dict(r=200)  # Add margin to the right for annotations
    )

    # Show the plot
    fig.show()


def get_latent_space(network, data):
    middle_layer = network.layers[len(network.layers) // 2]
    latent_space = []

    for d in data:
        output = d
        for layer in network.layers[:len(network.layers) // 2 + 1]:
            output = layer.activate(output)
        latent_space.append(output)

    return np.array(latent_space)

def interpolate_vectors(v1, v2, alpha=0.5):
    return v1 * (1 - alpha) + v2 * alpha

def decode_latent_vector(network, latent_vector):
    output = latent_vector
    for layer in network.layers[len(network.layers) // 2 + 1:]:
        output = layer.activate(output)
    return output

def save_letter_to_txt(letter, filename):
    letter_matrix = letter.reshape(7, 5)
    np.savetxt(filename, letter_matrix, fmt='%d', delimiter='')

def read_letter_from_txt(filename):
    return np.loadtxt(filename, dtype=int, delimiter='').reshape(7, 5)

def plot_new_letter():
    network = test_autoencoder()
    latent_space = get_latent_space(network, convert_to_35_array())

    # Interpolate between two characters
    character1 = latent_space[0]
    character2 = latent_space[1]

    new_latent_vector = interpolate_vectors(character1, character2, 0.5)
    output = decode_latent_vector(network, new_latent_vector)

    plt.imshow(output.reshape(7, 5), cmap='gray_r', interpolation='nearest')
    plt.title("Interpolated character")
    plt.axis('off')
    plt.show()

    save_letter_to_txt((output > 0.5).astype(int), 'new_letter.txt')

# csv_path = 'latent_space2.csv'
# save_latent_space_to_csv(test_autoencoder(), csv_path)
# plot_latent_space_from_csv(csv_path)
# test_autoencoder()

noise_array = [0, 0.05, 0.1, 0.15, 0.2]
correct_results = [32,27,24,15,11]

plt.plot(noise_array, correct_results)
plt.grid(color = 'gray')
plt.xlabel('Noise Level')
plt.ylabel('Correct Results')
plt.title('Effect of Noise Level on Correct Results')
plt.xticks(np.arange(0, 0.21, 0.05))
plt.yticks(np.arange(0, max(correct_results)+1, 5))
plt.show()
