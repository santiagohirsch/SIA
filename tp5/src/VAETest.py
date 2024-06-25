from matplotlib import pyplot as plt
import numpy as np

from Autoencoder import Autoencoder
from MultiLayer import MultiLayer
from Adam import Adam
from TrainingUtils import TrainingUtils
from font import get_characters
from icons import get_icons

BETA = 0.5
TAN_H = (lambda x: np.tanh(BETA * x) )
TAN_H_DERIVATIVE = (lambda x: (1 - np.tanh(BETA * x) ** 2)* BETA)

learning_rate = 0.0001

def test_vae():
    encoder = MultiLayer([100,80,60,40,20], TAN_H, TAN_H_DERIVATIVE, learning_rate, Adam)
    decoder = MultiLayer([10,20,40,60,80,100], TAN_H, TAN_H_DERIVATIVE, learning_rate, Adam)

    autoencoder = Autoencoder(encoder, decoder)

    icons = get_icons()
    test_set = np.array(icons.copy())

    autoencoder.train(test_set, 10000)

    # test
    z = autoencoder.encoder.test_forward_propagation(test_set)
    out,_ = reparametrize(z)
    out = autoencoder.decoder.test_forward_propagation(out)

    for i in range(len(test_set)):
        fig, axs = plt.subplots(1, 2, figsize=(15, 5))
        print("--------------------------------")
        print("Expected")
        axs[0].imshow(test_set[i].reshape(10, 10), cmap='gray_r', interpolation='nearest')
        axs[0].set_title("Expected")
        axs[0].axis('off')
        # print(test_set[i].reshape(10, 10))
        print("--------------------------------")
        print("Result")
        # print(out[i].reshape(10, 10))
        axs[1].imshow(out[i].reshape(10, 10), cmap='gray_r', interpolation='nearest')
        axs[1].set_title("Output")
        axs[1].axis('off')

        plt.show()

    return autoencoder

def reparametrize(data):
        mean = data[:, : data.shape[1] // 2]
        desviation = data[:, data.shape[1] // 2:]
        eps = np.random.standard_normal()
        return eps * desviation + mean, eps

def generate_new_emojis(autoencoder, num_samples=10):
    # Generar dos puntos aleatorios en el espacio latente
    z1 = np.random.normal(size=(2))
    z2 = np.random.normal(size=(2))

    # Interpolar entre z1 y z2
    z_interpolated = np.linspace(z1, z2, num_samples)

    # Decodificar las muestras interpoladas para generar nuevos emojis
    new_emojis = autoencoder.test(z_interpolated)
    
    return new_emojis

# Función para mostrar los nuevos emojis generados
def show_emojis(emojis):
    fig, axs = plt.subplots(1, len(emojis), figsize=(15, 5))
    for i, emoji in enumerate(emojis):
        axs[i].imshow(emoji.reshape(10, 10), cmap='gray')
        axs[i].axis('off')
    plt.show()


def latent_space(vae):
    latent_dim = vae.latent_space_size

    z = np.random.normal(size=(1, latent_dim))

    new_emoji = vae.test(z)

    plt.imshow(new_emoji.reshape(10,10), cmap='gray_r', interpolation='nearest')
    plt.title("Interpolated character")
    plt.axis('off')
    plt.show()

show_emojis(generate_new_emojis(test_vae()))