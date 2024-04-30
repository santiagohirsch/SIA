import numpy as np

from OptimizationMethod import OptimizationMethod

class GradientDescent(OptimizationMethod):
    @classmethod
    def calculate(self, expected_value: float, activation_value: float, training_value: np.ndarray,
                  activation_derivative=None, excitement=None):
        return (self.learning_rate * (expected_value - activation_value) * activation_derivative(excitement) * training_value)

    @classmethod
    def configure(self, learning_rate: float):
        super().configure(learning_rate)