import random

class Fists:
    damage = (1, 3)

    def __repr__(self):
        return 'Кулаки'

    def hit(self):
        return random.randint(*self.damage)

class Sword:
    damage = (3, 7)

    def __repr__(self):
        return 'Меч'

    def hit(self):
        return random.randint(*self.damage)

class Heal:

    def __repr__(self):
        return 'Лечение'
    def use_spell(self, target):
        target.hp += 3
        print(f'HP {target} - {target.hp}')

class Rare_sword:
    damage = (7, 11)

    def __repr__(self):
        return 'Редкий меч'

    def hit(self):
        return random.randint(*self.damage)









fist = Fists()

