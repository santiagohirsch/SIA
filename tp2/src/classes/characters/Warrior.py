from src.classes.characters.Character import Character

ATTACK_PCT = 0.6
DEFENSE_PCT = 0.4

class Warrior(Character):
    def __init__(self, attributes):
        super().__init__(ATTACK_PCT, DEFENSE_PCT, attributes)

    def __str__(self):
        return "Warrior" + super().__str__()