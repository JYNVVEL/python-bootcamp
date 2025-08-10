from .character import Character

class Warrior(Character):
    def __init__(self, strength):
        super().__init__()
        self._strength = strength

    def attack(self, other):
        damage = self._strength - other._defense
        other._health -= damage