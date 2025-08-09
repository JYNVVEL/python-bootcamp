class Character:
    def __init__(self, health=10, strength=10, defense=10):
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self, other):
        damage = self.strength - other.defense
        other.health -= damage

player = Character(strength=100)
enemy = Character()

player.attack(enemy)
print(enemy.health)