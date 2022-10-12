import PySimpleGUI as sg

from enemy import Goblin
from hero import Paladin
from pathlib import Path


def generate_down_panel(player):
    frame_feature = [
        [sg.Text(f'Здоровье: {player.hp} / {player.max_hp}', key='-HP-')],
        [sg.Text(f'Оружие в руках: {player.weapon}', key='-WEAPON-')],
        [sg.Text(f'Активное заклинание: {player.spell}', key='-SPELL-')],
    ]

    frame_inventary = [
        [sg.Button('Оружие', k='-INV_WEAPONS-')],
        [sg.Button('Заклинания', k='-INV_SPELLS-')],
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
        [sg.Button(weapon, key=player.weapons.index(weapon)) for weapon in player.weapons if
         player.weapons.index(weapon) % 3 == 0],
        [sg.Button(weapon, key=player.weapons.index(weapon)) for weapon in player.weapons if
         player.weapons.index(weapon) % 3 == 1],
        [sg.Button(weapon, key=player.weapons.index(weapon)) for weapon in player.weapons if
         player.weapons.index(weapon) % 3 == 2],
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
        prev_window['-WEAPON-'].Update(f'Оружие в руках: {player.weapon}')

    window.close()


def spells_window(player, prev_window):
    frame_spells = [
        [sg.Button(spell, key=player.spells.index(spell)) for spell in player.spells if
         player.spells.index(spell) % 3 == 0],
        [sg.Button(spell, key=player.spells.index(spell)) for spell in player.spells if
         player.spells.index(spell) % 3 == 1],
        [sg.Button(spell, key=player.spells.index(spell)) for spell in player.spells if
         player.spells.index(spell) % 3 == 2],
    ]
    layout = [
        [sg.Frame('Заклинания', frame_spells)]
    ]

    window = sg.Window('Заклинания', layout)
    while True:  # Главный цикл окна
        event, value = window.read()  # Считываются нажатия на кнопки
        if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
            break

        player.equip_spell(event)
        prev_window['-SPELL-'].Update(f'Активное заклинание: {player.spell}')

    window.close()

def fight(player: Paladin, enemy):
    ways = ["Ударить", "Колдовать", "Сбежать"]  # Указываем список событий
    # Служебные переменные для контроля за состоянием
    enemy_img = 'img/goblin.png'

    frame_enemy_feature = [
        [sg.Text(f'Здоровье: {enemy.hp} / {enemy.max_hp}', key='-HP_ENEMY-')],
    ]
    buttons = generate_button(ways)  # Из списка событий генерируются кнопки.
    down_panel = generate_down_panel(player)  # Генерируются нижняя панель
    down_panel[0].append(sg.Frame('Действия', buttons))  # К нижней панели добавляются кнопки
    down_panel[0].append(sg.Frame(enemy, frame_enemy_feature))
    layout = [
        [sg.Column([[sg.Image(source=enemy_img, key='-IMG-')]]),  # В source передавай путь к файлу
         sg.Output(key='-OUT-', size=(30, 1), expand_y=True, font=16)],
        [sg.Column(down_panel, element_justification='center')]
    ]

    window = sg.Window('Бой!', layout=layout, element_justification='center')  # Создаем объект окна приложения

    while True:  # Главный цикл окна
        event, value = window.read()  # Считываются нажатия на кнопки
        if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
            break
        if event == '-INV_WEAPONS-':
            weapons_window(player, window)
        if event == '-INV_SPELLS-':
            spells_window(player, window)

        if event == 'Ударить':
            damage = player.attack(enemy)
            window['-HP_ENEMY-'].Update(f'Здоровье: {enemy.hp} / {enemy.max_hp}')
            print(f'Вы нанесли {damage} урона врагу')
            if enemy.hp <= 0:
                sg.Popup('Вы победили!')
                break
            damage = enemy.attack(player)
            print(f'Вам нанесли {damage} урона')
            if player.hp <= 0:
                print('Вы погибли!')
                sg.Popup('Вы погибли!')
                break

            print(f"У врага осталось {enemy.hp} HP")

    window.close()

def main():
    weapons = ['seord', 'sdfgsdfg', 'ertwer', 'sdfg34t']
    pal = Paladin()
    pal.weapons = weapons
    gob = Goblin()
    fight(pal, gob)

if __name__ == '__main__':
    main()
