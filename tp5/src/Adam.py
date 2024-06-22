import numpy as np


class Adam:

    def __init__(self, learning_rate = 0.0001, beta1 = 0.9, beta2 = 0.99, epsilon = 1e-8):
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = None
        self.v = None

    def calculate(self, g, epoch):
        if self.m is None:
            self.m = np.zeros(np.shape(g))
            self.v = np.zeros(np.shape(g))
        print("g", g.shape)
        print("m", (1-self.beta1))
        self.m = self.beta1 * self.m 
        self.v = self.beta2 * self.v + (1 - self.beta2) * (g ** 2)
        m_hat = self.m / (1 - self.beta1 ** epoch + 1)
        v_hat = self.v / (1 - self.beta2 ** epoch + 1)
        return self.learning_rate * m_hat / (np.sqrt(v_hat) + self.epsilon)