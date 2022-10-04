import random

class Rat:
    hp = 7

    def attack(self, enemy):
        damage = random.randint(1, 2)
        enemy.hp -= damage
        return damage

class Goblin:
    hp = 15

    def attack(self, enemy):
        damage = random.randint(2, 4)
        enemy.hp -= damage
        return damage
