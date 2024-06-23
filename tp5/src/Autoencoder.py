import numpy as np
from MultiLayer import MultiLayer


class Autoencoder:

    # def __init__(self, latent_space_idx ,architecture, hidden_function, hidden_derivative, output_function, output_derivative,
    #              learning_rate=0.01, weight_distribution=(-1, 1), weights=None):
    #     super().__init__(architecture,hidden_function, hidden_derivative, output_function, output_derivative,learning_rate,weight_distribution, weights)
    #     self.latent_space_index = latent_space_idx

    def __init__(self, encoder:MultiLayer, decoder:MultiLayer):
        self.encoder = encoder
        self.decoder = decoder
        self.latent_space_size = decoder.layers[0].input_qty #- 1
        self.last_delta_size = decoder.layers[0].output_qty

    def get_latent_space_input(self, dataset):
        new_input = dataset
        for i in range(0,self.latent_space_index):
            new_input = self.layers[i].test_activation(new_input)
        return new_input
    
    def train(self, input, epochs, loss=None):
        for epoch in range(0, epochs):
            if epoch % 1000 == 0:
                print("Epoch: ", epoch)
            data = self.encoder.forward_propagation(input)

            mean = data[:, : data.shape[1] // 2]
            desviation = data[:, data.shape[1] // 2:]

            z, eps = self.reparametrize(mean, desviation)

            data = self.decoder.forward_propagation(z)

            reconstruction_error = self.reconstruction_error(input, data, mean, desviation)

            if loss is not None and reconstruction_error < loss:
                break

            decoder_deltas_w, decoder_last_delta = self.decoder.back_propagation(input - data)

            aux = np.ones([self.last_delta_size, self.latent_space_size])
            dot1 = np.dot(decoder_last_delta, aux)
            dot2 = np.dot(decoder_last_delta, eps * aux)
            encoder_reconstruction_deltas_w, _ = self.encoder.back_propagation(
                np.concatenate(
                    (dot1, dot2), axis=1
                )
            )

            encoder_loss_error, _ = self.encoder.back_propagation(
                np.concatenate(
                    (mean, 0.5 * (np.exp(desviation) ** 2 - 1)), axis=1
                )
            )

            encoder_deltas_w = []
            for d1, d2 in zip(encoder_reconstruction_deltas_w, encoder_loss_error):
                encoder_deltas_w.append(d1 + d2)

            
            self.encoder.update_weights(epoch, encoder_deltas_w) # TODO: check if this is correct
            self.decoder.update_weights(epoch, decoder_deltas_w)

    def reparametrize(self, mean, desviation):
        eps = np.random.standard_normal()
        return eps * desviation + mean, eps

    def reconstruction_error(self, input, output, mean, desviation):
        rec = 0.5 * np.mean((input - output) ** 2)
        kl = -0.5 * np.mean(1 + desviation - mean ** 2 - np.exp(desviation))
        return rec + kl
    
    def test(self, input): 
        return self.decoder.test_forward_propagation(input)