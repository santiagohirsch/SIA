from src.classes.characters.Character import Character

ATTACK_PCT = 0.1
DEFENSE_PCT = 0.9

class Defender(Character):
    def __init__(self, attributes):
        super().__init__(attributes, ATTACK_PCT, DEFENSE_PCT)

    def __str__(self):
        return "Defender" + super().__str__()