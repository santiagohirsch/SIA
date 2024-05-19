from neurons.Neuron import Neuron

class KohonenNeuron(Neuron):
    def __init__(self, x, y, weights):
        self.x = x
        self.y = y
        self.weights = weights

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y