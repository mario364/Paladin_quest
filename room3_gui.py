import PySimpleGUI as sg

from gui_template import generate_down_panel, generate_button
from minions import Imp
from hero import Paladin






def room3(player):
    mirarel_state = True
    imp1 = Imp()
    imp_state = True
    ways = ["Налево", "Направо", "Вперед"]

    buttons = generate_button(ways)  # Из списка событий генерируются кнопки.
    down_panel = generate_down_panel(player)  # Генерируются нижняя панель
    down_panel[0].append(sg.Frame('Действия', buttons))  # К нижней панели добавляются кнопки
    layout = [
        [sg.Column([[sg.Image(source='img/room3.png', key='-IMG-')]]),  # В source передавай путь к файлу
         sg.Output(key='-OUT-', size=(30, 1), expand_y=True, font=16)],
        [sg.Column(down_panel, element_justification='center')]
    ]

    window = sg.Window('Комната 3', layout=layout, element_justification='center')  # Создаем объект окна приложения

    while True:  # Главный цикл окна
        event, value = window.read()  # Считываются нажатия на кнопки
        if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
            break

        if event == 'Налево':
            window['-IMG-'].Update('img/god_of_luck.png')
            if not mirarel_state:
                print('Здесь только статуя.')

            if mirarel_state:
                print('Вы прошли до конца коридора и увидели статую. Напротив статую сидела эльфийка. Она подошла к вам'
                      '-"Здравствуй, паладин! Присядь рядом со мной и помолись богине удачи"')
                action = sg.PopupYesNo('Вы хотите помолиться?')
                if action == 'NO':
                    print('-"Я разочарована паладин." Сказала эльфийка и вы ушли.')
                    continue
                if action == "Yes":
                    print('Вы помолились богине удачи. -"Спасибо, паладин. Я увеличу твои силы"')
                    player.max_hp = 20
                    print(f"Ваше максимальное HP увеличено. HP = {player.max_hp}")
                mirarel_state = False
                continue


        if event == "Направо":
            if not imp_state:
                print('Здесь больше никого нет')
                continue
            if imp_state:
                window['-IMG-'].Update('img/imp.png')
                print('Вы прошли до конца коридора. И увидели чертёнка. Он выглядел дружелюбно. При виде вас,'
                      'он побежал и запрыгнул к вам на плечо. Оставите его?')
                action = sg.PopupYesNo('Вы хотите оставить чертенка?')
                if action == "No":
                    print('Вы смахнули чертёнка. Он обиженно посмотрел на вас и испарился')
                    continue
                if action == 'Yes':
                    print('Вы оставил чертёнка себе.')
                    player.minion = imp1
                imp_state = False
                continue
        if event == 'Вперед':
            print('Перед вами дверь.')
            action = sg.PopupYesNo('Вы хотите войти?')
            if action == 'Yes':
                print('Вы вошли в дверь')
                break
            else:
                print("Вы решили не входить")
                continue



pal1 = Paladin()
room3(pal1)








