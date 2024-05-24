
class HopfieldNeuron:
    def __init__(self, state: int, weights: list[float]):
        self.state = state
        self.weights = weights

    def get_weights(self):
        return self.weights
    
    def get_state(self):
        return self.state
    
    def set_state(self, state: int):
        self.state = state
    
    def set_weights(self, weights: list[float]):
        self.weights = weights