from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health=10, defense=10):
        self._health = health
        self._defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

    @property
    def health(self):
        return self.health