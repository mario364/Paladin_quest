import random
from hero import Paladin

class Rat:
    hp = 7
    max_hp = 7

    def __init__(self, gold=10, weapon=None):
        self.loot = {'gold': random.randint(1, gold), 'weapon': weapon}



    def __repr__(self):
        return 'Крыса'

    def attack(self, enemy):
        damage = random.randint(1, 2)
        enemy.hp -= damage
        return damage


class Goblin:
    hp = 15
    max_hp = 15
    img = 'img/zicon2.5.png'

    def __repr__(self):
        return 'Гоблин'

    def attack(self, enemy):
        damage = random.randint(2, 4)
        enemy.hp -= damage
        return damage


class Skelet:
    hp = 21
    max_hp = 15

    def __repr__(self):
        return 'Скелет'

    def attack(self, enemy):
        damage = random.randint(4, 10)
        enemy.hp -= damage
        return damage


