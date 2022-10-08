import PySimpleGUI as sg

from enemy import Goblin
from gui_template import generate_down_panel, generate_button
from hero import Paladin


def room2_window(player):
    ways = ['Пойти на звук', 'Дверь', 'Книга']  # Указываем список событий
    # Служебные переменные для контроля за состоянием
    door_state = False
    irdis_state = True
    bible_state = True
    gob = Goblin()


    buttons = generate_button(ways)  # Из списка событий генерируются кнопки.
    down_panel = generate_down_panel(player)  # Генерируются нижняя панель
    down_panel[0].append(sg.Frame('Действия', buttons))  # К нижней панели добавляются кнопки
    layout = [
        [sg.Column([[sg.Image(source='img/room2.png', key='-IMG-')]]),  # В source передавай путь к файлу
         sg.Output(key='-OUT-', size=(30, 1), expand_y=True, font=16)],
        [sg.Column(down_panel, element_justification='center')]
    ]

    window = sg.Window('Комната 2', layout=layout, element_justification='center')  # Создаем объект окна приложения

    while True:  # Главный цикл окна
        event, value = window.read()  # Считываются нажатия на кнопки
        if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
            break

        if event == "Пойти на звук":
            if irdis_state:
                print('Вы увидели умирающего старца на которого нападает гоблин')
                action = sg.PopupYesNo('Вы хотите помочь?')
                if action == 'No':
                    print('Вы ушли, бросив старца умирать. Разве паладины так поступают?..')
                else:
                    print('Вы вступили в бой с гоблином!')
                    # fight(player, goblin)
                    if player.hp < 0:
                        print('Вы проиграли!')
                        sg.Popup('Вы проиграли')
                        break
                    print("Спасибо, паладин! Дверь из этой комнаты можно открыть только если правильно постучать!"
                          "Старец дал вам код")
                    print('За помощь, я излечу твои раны =)')
                    player.hp = player.max_hp
                    print(f'Ваше здоровье полностью восстановлено')
                    door_state = True
            if not irdis_state:
                print('Старика больше нет.')

        if event == 'Дверь':
            if door_state:
                print('Вы вошли в дверь.')
                break
            if not door_state:
                print('Дверь не открывается')


        if event == 'Книга':
            window['-IMG-'].Update('img/bible.png')

            if bible_state:
                action = sg.PopupYesNo('Вы хотите прочитать?')
                if action == 'Yes':
                    print('Вы прочли книгу и расшифровали код от двери')
                    door_state = True
                if action == 'No':
                    print('ВЫ не прочитали книгу')
                    door_state = False

            if not bible_state:
                print('Вы уже прочли книгу')
    window.close()





pal = Paladin()
pal.weapons.extend(['sword', 'sword', 'sword'])
room2_window(pal)