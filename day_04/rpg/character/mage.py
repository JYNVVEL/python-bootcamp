from .character import Character

class Mage(Character):
    def __init__(self, magic):
        super().__init__()
        self._magic = magic

    def attack(self, other):
        damage = self._magic - other._defense
        other._health -= damage