from character.knight import Knight
from character.warrior import Warrior
from character.mage import Mage

mage = Mage(100)
knight = Knight()
warrior = Warrior(200)

mage.attack(knight)
print(knight._health)

