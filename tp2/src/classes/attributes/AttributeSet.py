from src.classes.attributes.Agility import Agility
from src.classes.attributes.Strength import Strength
from src.classes.attributes.Expertise import Expertise
from src.classes.attributes.Endurance import Endurance
from src.classes.attributes.Health import Health
from src.classes.attributes.Height import Height

class AttributeSet:
    def __init__(self, agility: float, strength: float, expertise: float, endurance: float, health: float, height: float):
        self.agility = Agility(agility)
        self.strength = Strength(strength)
        self.expertise = Expertise(expertise)
        self.endurance = Endurance(endurance)
        self.health = Health(health)
        self.height = Height(height)

    def get_agility(self) -> Agility:
        return self.agility

    def get_strength(self) -> Strength:
        return self.strength
    
    def get_expertise(self) -> Expertise:
        return self.expertise

    def get_endurance(self) -> Endurance:
        return self.endurance
    
    def get_health(self) -> Health:
        return self.health
    
    def get_height(self) -> Height:
        return self.height

    def to_array(self) -> list:
        return [self.agility.value, self.strength.value, self.expertise.value, self.endurance.value, self.health.value, self.height.value]

    @staticmethod
    def from_array(array: list):
        return AttributeSet(array[0], array[1], array[2], array[3], array[4], array[5])

    def __str__(self) -> str:
        return f"\nAgility: {self.agility} | Strength: {self.strength} | Expertise: {self.expertise} | Endurance: {self.endurance} | Health: {self.health} | Height: {self.height}"