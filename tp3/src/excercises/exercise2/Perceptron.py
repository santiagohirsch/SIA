from abc import ABC, abstractmethod
import numpy as np

class Perceptron(ABC):

    def excitement(weights, training):
        return np.dot(weights, training)
    
    @abstractmethod
    def activation(excitement):
        pass

    @abstractmethod
    def delta(activation, training, expected):
        pass

    @abstractmethod
    def error(training_set, expected_set):
        pass