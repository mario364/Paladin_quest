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


fist = Fists()

