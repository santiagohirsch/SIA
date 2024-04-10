from math import tanh
import math
from src.classes.attributes.Attribute import Attribute

class Health(Attribute):
    def __init__(self, value):
        super().__init__(value)

    def get_p(self):
        return 100 * tanh(0.01 * self.value)
    
    def __str__(self):
        return super().__str__()
    
    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Health):
            return math.isclose(other.value, self.value, rel_tol=1e-03)
        else:
            return False