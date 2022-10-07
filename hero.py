from weapons import Fists, Heal
from func import get_action


class Paladin:
    max_hp = 15
    hp = 15
    weapons = [Fists()]
    weapon = 'Нет'
    spell = 'Нет'
    spells = [Heal()]


    def __repr__(self):
        return 'Герой'

    def equip(self, index):
        self.weapon = self.weapons[index]

    def attack(self, enemy):
        damage = self.weapon.hit()
        enemy.hp -= damage
        return damage

    def wiz(self, index, target):
        self.spells[index].use_spell(target)


player = Paladin()
