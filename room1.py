from gui_class import sg, Window, WeaponInventory, SpellsInventory
from hero import Paladin


class Room1(Window):

    def main_loop(self, window):
        lever_state = False

        while True:  # Главный цикл окна
            event, value = window.read()  # Считываются нажатия на кнопки
            if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
                break
            if event == '-INV_WEAPONS-':
                WeaponInventory(window, self.player).show()
            if event == '-INV_SPELLS-':
                SpellsInventory(window, self.player).show()
            if event == 'Сундук':
                pass

            if event == 'Рычаг':
                print('Вы подошли к рычагу.')
                if lever_state:
                    print('Рычаг заклинило')
                else:
                    window['-IMG-'].Update('img/lever.png')
                    action = sg.PopupYesNo('Вы хотите нажать на рычаг?')
                    if action == 'No':
                        print('Вы решили не рисковать')
                    if action == 'Yes':
                        print('Вы дернули рычаг и услышали звук механизма. Но откуда шел звук?')
                        lever_state = True

            if event == 'Дверь':
                if lever_state:
                    action = sg.PopupYesNo('Вы хотите зайти?')
                    if action == 'Yes':
                        print('Вы вышли')
                        break
                if not lever_state:
                    print('Дверь закрыта')

pal = Paladin()
pal.spells = ['asdf', 'asdfer']
test_room = Room1(player=pal, ways=["Сундук", "Рычаг", "Дверь"], title_room='Тестовая комната')
test_room.show()