from weapons import Fists, Heal
import random

class Paladin:
    max_hp = 15
    hp = 15
    gold = 0
    weapons = [Fists()]
    weapon = Fists()
    spell = 'Нет'
    spells = [Heal()]
    minion = None


    def __repr__(self):
        return 'Герой'

    def equip(self, index):
        self.weapon = self.weapons[index]

    def equip_spell(self, index):
        self.spell = self.spells[index]

    def attack(self, enemy):
        damage = self.weapon.hit()
        if self.minion:
            damage += self.minion.buff()
        enemy.hp -= damage
        return damage

    def wiz(self, index, target):
        self.spells[index].use_spell(target)


player = Paladin()
