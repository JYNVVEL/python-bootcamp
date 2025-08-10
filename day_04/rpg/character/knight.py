from .character import Character

class Knight(Character):
    def attack(self, other):
        damage = self._defense - other._defense
        other._health -= damage