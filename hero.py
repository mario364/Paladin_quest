from weapons import Fists
from func import get_action


class Paladin:
    max_hp = 15
    hp = 15
    weapons = [Fists()]
    weapon = None

    def equip(self):
        print('Доступное оружие: ')
        action = get_action(self.weapons, 'Оружие')
        self.weapon = self.weapons[action - 1]

    def attack(self, enemy):
        damage = self.weapon.hit()
        enemy.hp -= damage
        return damage


player = Paladin()

