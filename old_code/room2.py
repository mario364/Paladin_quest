from func import get_action, fight
from enemy import Goblin

yes_no = '\n1 - Да\n2 - Нет '


def room2(player):
    goblin = Goblin()
    events = ['Пойти на звук', 'Дверь', 'Книга']
    door_code = False
    irdis = True
    bible = True
    print('Вы вошли во вторую комнату, вам кажется, что задание слишком простое')

    while True:
        action = get_action(events)

        if action == 1:
            if irdis:
                print('Вы увидели умирающего старца на которого нападает гоблин')
                action = input('Вы хотите помочь старцу?' + yes_no)
                if action == '2':
                    print('Вы ушли, бросив старца умирать. Разве паладины так поступают?..')
                else:
                    print('Вы вступили в бой с гоблином!')
                    fight(player, goblin)
                    if player.hp < 0:
                        print('Вы проиграли!')
                        break
                    print("Спасибо, паладин! Дверь из этой комнаты можно открыть только если правильно постучать!"
                          "Старец дал вам код")
                    print('За помощь, я излечу твои раны =)')
                    player.hp = player.max_hp
                    print(f'Ваше здоровье полностью восстановлено')
                    door_code = True

                irdis = False
            else:
                print('Старика больше нет')

        if action == 2:
            if bible:
                print('Вы увидели книгу.')
                action = int(input("Хотите ее прочитать? " + yes_no))
                if action == 2:
                    print('Вы не прочли книгу')
                    continue
                if action == 1:
                    print('Вы прочли книгу и расшифровали тайное послание, теперь вы знаете как открыть дверь')
                    door_code = True
                bible = False
            if not bible:
                print('Книга уже прочитана')
            continue
        if action == 3:
            if not door_code:
                print('Дверь не открывается')
                continue
            if door_code:
                print("Вы вышли из комнаты")
                break
