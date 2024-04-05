from math import tanh
from src.classes.attributes.Attribute import Attribute

class Height(Attribute):
    def __init__(self, value):
        super().__init__(value)

    def get_ATM(self):
        return 0.5 - (3 * self.value - 5) ** 4 + (3 * self.value - 5) ** 2 + self.value / 2
    
    def get_DEM(self):
        return 2 + (3 * self.value - 5) ** 4 - (3 * self.value - 5) ** 2 - self.value / 2