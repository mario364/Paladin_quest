import PySimpleGUI as sg
from hero import Paladin
from pathlib import Path


def generate_down_panel(player):
    frame_feature = [
        [sg.Text(f'Здоровье: {player.hp} / {player.max_hp}', key='-HP-')],
        [sg.Text(f'Оружие в руках: {player.weapon}', key='-WEAPON-')],
    ]

    frame_weapons = [
        [sg.Text(weapon) for weapon in player.weapons if player.weapons.index(weapon) % 3 == 0],
        [sg.Text(weapon) for weapon in player.weapons if player.weapons.index(weapon) % 3 == 1],
        [sg.Text(weapon) for weapon in player.weapons if player.weapons.index(weapon) % 3 == 2],
    ]

    frame_spells = [
        [sg.Text(spell) for spell in player.spells]
    ]

    down_panel = [
        [sg.Frame("Характеристики Героя", frame_feature),
         sg.Frame("Оружие", frame_weapons, k='-WEAPONS-'),
         sg.Frame('Заклинания', frame_spells),
         ]
    ]

    return down_panel


def generate_button(events):
    buttons = [
        [sg.Button(event) for event in events if events.index(event) % 2 == 0],
        [sg.Button(event) for event in events if events.index(event) % 2 == 1],
    ]
    return buttons


def main():
    pass


if __name__ == '__main__':
    main()
