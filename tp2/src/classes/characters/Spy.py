from src.classes.characters.Character import Character

ATTACK_PCT = 0.8
DEFENSE_PCT = 0.3

class Spy(Character):
    def __init__(self, attributes):
        super().__init__(attributes, ATTACK_PCT, DEFENSE_PCT)