class Character:
    def __init__(self, health=10, strength=10, defense=10):
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self, other):
        damage = self.strength - other.defense
        other.health -= damage


class Knight:
    def __init__(self, health=10, defense=10):
        self.health = health
        self.defense = defense

    def attack(self, other):
        damage = self.defense - other.defense
        other.health -= damage

player = Knight(defense=100)
enemy = Character()
player.attack(enemy)
print(enemy.health)