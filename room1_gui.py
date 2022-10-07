import random
import PySimpleGUI as sg

from enemy import Rat
from gui_template import generate_down_panel, generate_button
from hero import Paladin
from weapons import Sword


def room1_window(player):
    events = ["Сундук", "Рычаг", "Дверь"]  # Указываем список событий
    # Служебные переменные для контроля за состоянием
    chest_state = False
    lever_state = False

    buttons = generate_button(events)  # Из списка событий генерируются кнопки.
    down_panel = generate_down_panel(player)  # Генерируются нижняя панель
    down_panel[0].append(sg.Frame('Действия', buttons))  # К нижней панели добавляются кнопки
    layout = [
        [sg.Column([[sg.Image(source='img/room.png', key='-IMG-')]]),  # В source передавай путь к файлу
         sg.Output(key='-OUT-', size=(30, 1), expand_y=True, font=16)],
        [sg.Column(down_panel, element_justification='center')]
    ]

    window = sg.Window('Комната 1', layout=layout, element_justification='center')  # Создаем объект окна приложения

    while True:  # Главный цикл окна
        event, value = window.read()  # Считываются нажатия на кнопки
        if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
            break

        if event == 'Сундук':
            if chest_state:
                print('Сундук открыт и пуст')
            else:
                chest_state = chest(player, window)

        if event == 'Рычаг':
            if lever_state:
                print('Рычаг заклинило')
            else:
                lever_state = lever(window)

    window.close()


def chest(player, window):
    sword = Sword()
    rat = Rat()
    chest_stuff = [None, sword, rat]
    window['-IMG-'].Update('img/Chest.png')

    stuff = random.choice(chest_stuff)
    if not stuff:
        print("В сундуке пусто")
    if stuff == sword:
        print("Вы нашли меч")
        player.weapons.append(sword)
    if stuff == rat:
        print('В сундуке была крыса!')
        # fight(player, rat)
    return True


def lever(window):
    window['-IMG-'].Update('img/lever.png')
    # window[]
    print('Вы подошли к рычагу.')
    action = sg.PopupYesNo('Вы хотите нажать на рычаг?')
    if action == 'No':
        print('Вы решили не рисковать')
        return False
    if action == 'Yes':
        print('Вы дернули рычаг и услышали звук механизма. Но откуда шел звук?')
        return True


pal = Paladin()
w = ['shield', 'sword', 'bow']
pal.weapons.extend(w)

room1_window(pal)
