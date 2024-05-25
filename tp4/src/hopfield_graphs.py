from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from algorithms.Hopfield import Hopfield

def parse_letters():
    df = pd.read_csv("../data/letters.txt", delimiter='  ', header=None)
    matrix_list = [df.iloc[i:i + 5, :] for i in range(0, len(df), 5)]
    matrix_based_arrays = [matrix.values.flatten() for matrix in matrix_list]
    return matrix_based_arrays

def add_noise(letter, noise_percentage):
    noise = np.random.choice([1, -1], size=letter.shape, p=[1 - noise_percentage, noise_percentage])
    return np.multiply(letter, noise)

def invert(letter):
    return np.multiply(letter, -1)

def hopfield(letters):
    input_state = add_noise(letters[4], 0.1)
    # input_state = invert(letters[1])
    network = Hopfield(letters[3:7], input_state)
    energy_array = network.train(5)
    df = pd.DataFrame({'Epoch': range(1, len(energy_array)+1), 'Energy': energy_array})
    df.to_csv('energy_per_epoch.csv', index=False)

def plot_energy_per_epoch():
    df = pd.read_csv('energy_per_epoch.csv')
    df.plot(x='Epoch', y='Energy', title='Energy per epoch', xlabel='Epoch', ylabel='Energy')
    plt.show()

def plot_letters():
    letters = parse_letters()
    for j in range(0, len(letters) - 2, 4):
        fig, axs = plt.subplots(2, 2)
        for i in range(j, j+4):
            aux = i % 4
            axs[aux//2, aux%2].imshow(-letters[i].reshape(5, 5), cmap='gray', vmin=-1, vmax=1)
            axs[aux//2, aux%2].set_xticks([])
            axs[aux//2, aux%2].set_yticks([])
            axs[aux//2, aux%2].set_facecolor('white')
        plt.show()
    letters = parse_letters()
    fig, axs = plt.subplots(1, 2)
    for i in range(len(letters)-2, len(letters)):
        axs[i-(len(letters)-2)].imshow(-letters[i].reshape(5, 5), cmap='gray', vmin=-1, vmax=1)
        axs[i-(len(letters)-2)].set_xticks([])
        axs[i-(len(letters)-2)].set_yticks([])
        axs[i-(len(letters)-2)].set_facecolor('white')
    plt.show()

def calculate_best_combo():
    letters = parse_letters()
    combos = [[0] * len(letters) for _ in range(len(letters))]
    for i in range(len(letters)):
        for j in range(len(letters)):
            if i == j:
                combos[i][j] = 0
                continue
            combos[i][j] = np.dot(letters[i], letters[j])

    for i in range(len(letters)):
        if 1 in combos[i]:
            letter_index = i
            matching_letters = [index for index, value in enumerate(combos[i]) if value == 1]
            print(f"Letter {chr(ord('A') + letter_index)} matches with letters {', '.join(chr(ord('A') + index) for index in matching_letters)}")
    # print(np.reshape(combos, (len(letters), len(letters))))

# hopfield(parse_letters())
# plot_energy_per_epoch()
# plot_letters()
calculate_best_combo()