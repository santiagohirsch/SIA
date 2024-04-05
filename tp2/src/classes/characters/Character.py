from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, attack_pct: int, defense_pct: int, attribute):
        self.attack_pct = attack_pct
        self.defense_pct = defense_pct
        self.attribute = attribute

    def get_attribute(self):
        return self.attribute

    # HACER
    @abstractmethod
    def attack(self):
        return (self.attribute)

    # HACER
    @abstractmethod
    def defend(self, character):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def fitness(self):
        return self.attack_pct * self.attack() + self.defense_pct * self.defend()

    def __lt__(self, other):
        return self.fitness < other.fitness
    
    def __eq__(self, other):
        return self.attribute == other.attribute