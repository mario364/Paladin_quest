import random
from func import get_action, fight
from weapons import Sword
from enemy import Rat


yes_no = '\n1 - Да\n2 - Нет '

def room1(player):
    sword = Sword()
    rat = Rat()
    events = ["Сундук", "Рычаг", "Дверь"]
    chest_stuff = [None, sword, rat]
    chest_open = False
    lever = False

    print('Вы вошли в первую комнату.')
    while True:
        action = get_action(events)

        if action == 1:
            if chest_open:
                print('Сундук открыт и пуст')
            else:
                chest_open = True
                stuff = random.choice(chest_stuff)
                if not stuff:
                    print("В сундуке пусто")
                if stuff == sword:
                    print("Вы нашли меч")
                    player.weapons.append(sword)
                if stuff == rat:
                    print('В сундуке была крыса!')
                    fight(player, rat)
            continue

        if action == 2:
            print('Вы подошли к рычагу.')
            action = input('Дернуть?' + yes_no)
            if lever:
                print('Рычаг заклинило')
                continue
            if action == '2':
                print('Вы решили не рисковать')
                continue
            else:
                print('Вы дернули рычаг и услышали звук механизма. Но откуда шел звук?')
                lever = True
                continue

        if action == 3:
            print("Вы подошли к двери")
            if not lever:
                print('Дверь закрыта')
                continue
            else:
                action = input('Хотите зайти?' + yes_no)
                if action == '1':
                    break
                else:
                    continue

