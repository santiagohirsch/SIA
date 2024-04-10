from src.classes.attributes.Agility import Agility
from src.classes.attributes.Strength import Strength
from src.classes.attributes.Expertise import Expertise
from src.classes.attributes.Endurance import Endurance
from src.classes.attributes.Health import Health
from src.classes.attributes.Height import Height

class AttributeSet:
    def __init__(self, agility: float, strength: float, expertise: float, endurance: float, health: float, height: float):
        total = agility + strength + expertise + endurance + health
        modifier = 150 / total
        self.agility = Agility(agility * modifier)
        self.strength = Strength(strength * modifier)
        self.expertise = Expertise(expertise * modifier)
        self.endurance = Endurance(endurance * modifier)
        self.health = Health(health * modifier)
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

    def __eq__(self, other) -> bool:
        if not isinstance(other, AttributeSet):
            return False
        return self.agility == other.agility and self.strength == other.strength and self.expertise == other.expertise and self.endurance == other.endurance and self.health == other.health and self.height == other.height