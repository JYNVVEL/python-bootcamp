from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, health=10, defense=10):
        self._health = health
        self._defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

class Knight(Character):
    def attack(self, other):
        damage = self._defense - other._defense
        other._health -= damage

class Warrior(Character):
    def __init__(self, strength):
        super().__init__()
        self._strength = strength

    def attack(self, other):
        damage = self._strength - other._defense
        other._health -= damage

class Mage(Character):
    def __init__(self, magic):
        super().__init__()
        self._magic = magic

    def attack(self, other):
        damage = self._magic - other._defense
        other._health -= damage

knight_1 = Knight()
warrior_1 = Warrior(20)
mage_1 = Mage(30)

knight_1.attack(warrior_1)
knight_1.attack(mage_1)

warrior_1.attack(knight_1)

print(warrior_1._health)
print(mage_1._health)

print(knight_1._health)
