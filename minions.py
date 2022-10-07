import random

class Imp:
    damage = (10, 11)

    def buff(self):
        return random.randint(*self.damage)