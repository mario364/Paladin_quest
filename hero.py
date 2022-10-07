from weapons import Fists, Heal
from func import get_action


class Paladin:
    max_hp = 15
    hp = 15
    weapons = [Fists()]
    weapon = None
    spells = [Heal()]

    def __repr__(self):
        return 'Герой'

    def equip(self):
        print('Доступное оружие: ')
        action = get_action(self.weapons, 'Оружие')
        self.weapon = self.weapons[action - 1]

    def attack(self, enemy):
        damage = self.weapon.hit()
        enemy.hp -= damage
        return damage

    def wiz(self, target):
        print('Выберите заклинание')
        action = get_action(self.spells, 'Заклинания')
        self.spells[action - 1].use_spell(target)


player = Paladin()
