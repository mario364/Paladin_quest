import random

class Weapon:
    damage = (0, 0)
    def hit(self):
        return random.randint(*self.damage)


class Fists(Weapon):
    damage = (1, 3)

    def __repr__(self):
        return 'Кулаки'


class Sword(Weapon):
    damage = (3, 7)

    def __repr__(self):
        return 'Меч'

class Heal:

    def __repr__(self):
        return 'Лечение'
    def use_spell(self, target):
        target.hp += 3
        print(f'HP {target} - {target.hp}')

class Rare_sword(Weapon):
    damage = (7, 11)

    def __repr__(self):
        return 'Редкий меч'

    def hit(self):
        return random.randint(*self.damage)









fist = Fists()

