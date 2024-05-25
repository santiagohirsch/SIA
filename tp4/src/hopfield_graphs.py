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
    input_state = add_noise(letters[2], 0.1)
    network = Hopfield(letters, input_state)
    energy_array = network.train(5)
    df = pd.DataFrame({'Epoch': range(1, len(energy_array)+1), 'Energy': energy_array})
    df.to_csv('energy_per_epoch.csv', index=False)

def plot_energy_per_epoch():
    df = pd.read_csv('energy_per_epoch.csv')
    df.plot(x='Epoch', y='Energy', title='Energy per epoch', xlabel='Epoch', ylabel='Energy')
    plt.show()

hopfield(parse_letters())
plot_energy_per_epoch()