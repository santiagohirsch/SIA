from abc import ABC, abstractmethod

import numpy as np


class Optimization(ABC):

    learning_rate = None

    @classmethod
    @abstractmethod
    def calculate(self, expected_value: float, activation_value: float, training_value: np.ndarray):
        pass

    @classmethod
    def configure(self, learning_rate: float):
        if learning_rate is None:
            raise ValueError("No learning rate provided")
        self.learning_rate = learning_rate
        pass