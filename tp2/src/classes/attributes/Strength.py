from math import tanh
from src.classes.attributes.Attribute import Attribute

class Strength(Attribute):
    def __init__(self, value):
        super().__init__(value)

    def get_p(self):
        return 100 * tanh(0.01 * self.value)

    def __str__(self):
        return super().__str__()
    