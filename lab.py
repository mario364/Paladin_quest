import random

import weapons
from hero import Paladin
from weapons import Sword, Rare_sword


def get_action(ways, title='Действия'):
    print(f' {title} '.center(21, '_'))
    for num, event in enumerate(ways, 1):
        print('|', f'{num} {event}'.center(17), '|')
    print(''.center(21, '_'))
    action = int(input("Что сделать? "))
    return action


def fight(player, enemy):
    print('Вы вступили в бой!')
    print(f'У вас осталось {player.hp} HP')
    events = ["Ударить", "Сменить оружие", 'Колдовать', "Сбежать"]
    while True:
        action = get_action(events)
        if action == 1:
            if not player.weapon:
                print("У вас нет оружия в руках!")
                print('Доступное оружие: ')
                action = get_action(player.weapons, 'Оружие')
                player.equip(action - 1)
            damage = player.attack(enemy)
            print(f'Вы нанесли {damage} урона врагу')
            if enemy.hp <= 0:
                print('Вы победили!')
                player.exp += enemy.exp
                print(f'Вы получили: {enemy.exp} единиц опыт. Ваша опыт {player.exp}')
                if player.exp >= 10:
                    print(f'Вы подняли уровень! У вас повысилось HP. Ваше HP: {player.max_hp + 10}')
                    player.exp = 0
                    player.max_hp += 10
                for i in enemy.loot:
                    print(f'Вы нашли {rat1.loot[i]} золотых')
                    if i == 'gold':
                        pal.gold += rat1.loot[i]
                        print(f'Общее кол-во золота {pal.gold}')
                    if i == 'weapon':
                        pal.weapons.append(rat1.loot[i])
                        print(f'Оружие в инвентаре: {pal.weapons}')

                break
            print(f"У врага осталось {enemy.hp} HP")
        if action == 2:
            action = get_action(player.weapons)
            player.equip(action - 1)
            continue

        if action == 3:
            print('Выберите заклинание')
            action = get_action(player.spells, 'Заклинания')
            target = int(input(f'1 - {enemy}\n2 - {player}\nВыберите цель: '))
            if target == 1:
                target = enemy
            if target == 2:
                target = player
            player.wiz(action - 1, target)

        damage = enemy.attack(player)
        print(f'Вам нанесли {damage} урона')
        if player.hp <= 0:
            print('Вы погибли!')
            break
        print(f'У вас осталось {player.hp} HP')


class Rat:
    hp = 7
    max_hp = 7
    exp = random.randint(3, 7)

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

    def __init__(self, gold=30, weapon=None):
        self.loot = {'gold': random.randint(1, gold), 'weapon': weapon}

    def __repr__(self):
        return 'Гоблин'

    def attack(self, enemy):
        damage = random.randint(2, 4)
        enemy.hp -= damage
        return damage


sword1 = Sword()
sword2 = Rare_sword()
pal = Paladin()
pal.weapon = sword1
rat1 = Rat(weapon=sword1)
gob = Goblin(weapon=random.choice([sword1, sword2]))

fight(pal, rat1)
fight(pal, gob)
