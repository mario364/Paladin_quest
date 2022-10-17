import random

class Enemy:
    damage = (0, 0)
    def attack(self, enemy):
        if enemy.armor:
            damage = random.randint(*self.damage) - enemy.armor.defense
            if damage < 0:
                damage = 0
        else:
            damage = random.randint(*self.damage)
        enemy.hp -= damage
        return damage

class Rat(Enemy):
    damage = (1, 2)
    img = 'img/rat.png'
    exp = 10
    max_hp = 7
    def __repr__(self):
        return 'Крыса'

    def __init__(self, loot=None):
        self.loot = loot
        self.hp = self.max_hp


class Goblin(Enemy):
    damage = (2, 5)
    max_hp = 15
    img = 'img/zicon2.5.png'
    exp = 20
    def __init__(self, loot=None):
        self.loot = loot
        self.hp = self.max_hp
    def __repr__(self):
        return 'Гоблин'



class Skelet:
    hp = 21
    max_hp = 15

    def __repr__(self):
        return 'Скелет'

    def attack(self, enemy):
        damage = random.randint(4, 10)
        enemy.hp -= damage
        return damage


