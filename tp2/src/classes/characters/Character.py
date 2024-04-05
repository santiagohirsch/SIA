from abc import ABC, abstractmethod
from src.classes.attributes.AttributeSet import AttributeSet

class Character(ABC):
    def __init__(self, attack_pct: int, defense_pct: int, attributes: AttributeSet):
        self.attack_pct = attack_pct
        self.defense_pct = defense_pct
        self.attributes = attributes

    def get_attribute(self):
        return self.attribute

    # HACER
    @abstractmethod
    def attack(self):
        return (self.attributes.get_agility().get_p() + self.attributes.get_expertise().get_p()) * self.attributes.get_strength().get_p() * self.attributes.get_height().get_ATM()

    # HACER
    @abstractmethod
    def defend(self):
        return (self.attributes.get_endurance().get_p() + self.attributes.get_expertise().get_p()) * self.attributes.get_health().get_p() * self.attributes.get_height().get_DEM()

    @abstractmethod
    def __str__(self):
        return self.attributes.__str__()

    def fitness(self):
        return self.attack_pct * self.attack() + self.defense_pct * self.defend()

    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def __eq__(self, other):
        return self.attributes == other.attributes