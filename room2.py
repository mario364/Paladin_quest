from func import get_action, fight
from enemy import Goblin

yes_no = '\n1 - Да\n2 - Нет '


def room2(player):
    goblin = Goblin()
    events = ['Пойти на звук', 'Дверь', 'Книга']
    door_code = False
    irdis = True
    bible = False
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

        if action == '2':
            if not bible:
                print('Вы увидели книгу.' + yes_no)
                action = input("Хотите ее прочитать? ")
        if action == '3':
            pass
