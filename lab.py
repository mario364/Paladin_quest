from hero import Paladin
from Boss_fight import boss_room
from minions import Imp
from gui_template import sg

pal = Paladin()
imp1 = Imp()
pal.weapons = ['asdf', 'sdfgs','1231' , 'sdgfsg']
pal.minion = imp1


def show_window(player):
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
    main_loop(window, player)


def main_loop(window, player):
    while True:  # Главный цикл окна
        event, value = window.read()  # Считываются нажатия на кнопки
        if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
            break

        player.equip(event)
        # window['-WEAPON-'].Update(f'Оружие в руках: {player.weapon}')
        break

print(pal.weapon)
show_window(pal)
print(pal.weapon)
