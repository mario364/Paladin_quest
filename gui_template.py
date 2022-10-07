import PySimpleGUI as sg
from hero import Paladin
from pathlib import Path


def generate_down_panel(player):
    frame_feature = [
        [sg.Text(f'Здоровье: {player.hp} / {player.max_hp}', key='-HP-')],
        [sg.Text(f'Оружие в руках: {player.weapon}', key='-WEAPON-')],
        [sg.Text(f'Активное заклинание: {player.weapon}', key='-SPELL-')],
    ]

    frame_weapons = [
        [sg.Text(weapon) for weapon in player.weapons if player.weapons.index(weapon) % 3 == 0],
        [sg.Text(weapon) for weapon in player.weapons if player.weapons.index(weapon) % 3 == 1],
        [sg.Text(weapon) for weapon in player.weapons if player.weapons.index(weapon) % 3 == 2],
    ]

    frame_inventary = [
        [sg.Button('Оружие', k='-INV-')],
        [sg.Button('Заклинания')],
    ]

    down_panel = [
        [sg.Frame("Характеристики Героя", frame_feature),
         sg.Frame('Инвентарь', frame_inventary),
         ]
    ]

    return down_panel


def generate_button(events):
    buttons = [
        [sg.Button(event) for event in events if events.index(event) % 2 == 0],
        [sg.Button(event) for event in events if events.index(event) % 2 == 1],
    ]
    return buttons

def weapons_window(player, prev_window):
    frame_weapons = [
        [sg.Button(weapon, key=player.weapons.index(weapon)) for weapon in player.weapons if player.weapons.index(weapon) % 3 == 0],
        [sg.Button(weapon, key=player.weapons.index(weapon)) for weapon in player.weapons if player.weapons.index(weapon) % 3 == 1],
        [sg.Button(weapon, key=player.weapons.index(weapon)) for weapon in player.weapons if player.weapons.index(weapon) % 3 == 2],
    ]
    layout = [
        [sg.Frame('Оружие', frame_weapons)]
    ]

    window = sg.Window('Инвентарь', layout)
    while True:  # Главный цикл окна
        event, value = window.read()  # Считываются нажатия на кнопки
        if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
            break

        player.equip(event)
        prev_window['-WEAPON-'].Update(player.weapon)

    window.close()

def main():
    weapons = ['seord','sdfgsdfg', 'ertwer', 'sdfg34t']
    pal = Paladin()
    pal.weapons = weapons
    weapons_window(pal, )


if __name__ == '__main__':
    main()
