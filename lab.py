from hero import Paladin
from gui_class import sg, Window, Fight

lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.' \
        ' Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor '\
        'in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,'\
        ' sunt in culpa qui officia deserunt mollit anim id est laborum.'


# class Fight(Window):
#     title_room = 'Битва'
#     ways = ["Ударить", "Колдовать", "Сбежать"]
#     _print_ = False
#
#     def __init__(self, player, enemy):
#         super().__init__(player)
#         self.enemy = enemy
#         self.extend_down_panel()
#
#     def extend_down_panel(self):
#         frame_enemy_feature = [
#             [sg.Text(f'Здоровье: {self.enemy.hp} / {self.enemy.max_hp}', key='-HP_ENEMY-')],
#         ]
#         self.down_panel[0].append(sg.Frame(self.enemy, frame_enemy_feature))


class Room1(Window):
    _print_ = False
    lever_state = False
    ways = ["Сундук", "Рычаг", "Дверь"]
    title_room = 'Комната 1'
    start_message = 'Вы вошли в первую комнату'

    def main_loop(self, window, event, value):
        if event == 'Сундук':
            Fight(pal, Rat()).show()

        if event == 'Рычаг':
            print('Вы подошли к рычагу.')
            if self.lever_state:
                window['-OUT-'].Update('Рычаг заклинило')
                print('Рычаг заклинило')
            else:
                window['-IMG-'].Update('img/lever.png')
                action = sg.PopupYesNo('Вы хотите нажать на рычаг?')
                if action == 'No':
                    window['-OUT-'].Update('Вы решили не рисковать')
                    print('Вы решили не рисковать')
                if action == 'Yes':
                    window['-OUT-'].Update('Вы дернули рычаг и услышали звук механизма. Но откуда шел звук?')
                    print('Вы дернули рычаг и услышали звук механизма. Но откуда шел звук?')
                    self.lever_state = True

        if event == 'Дверь':
            if self.lever_state:
                action = sg.PopupYesNo('Вы хотите зайти?')
                if action == 'Yes':
                    window['-OUT-'].Update('Вы вышли')
                    print('Вы вышли')
                    window.close()
            if not self.lever_state:
                window['-OUT-'].Update('Дверь закрыта')
                print('Дверь закрыта')

class Room1_noprint(Window):
    _print_ = False
    lever_state = False
    ways = ["Сундук", "Рычаг", "Дверь"]
    title_room = 'Комната 1'
    start_message = 'Вы вошли в первую комнату'

    def main_loop(self, window, event, value):
        if event == 'Сундук':
            Fight(pal, Rat()).show()

        if event == 'Рычаг':
            window['-OUT-'].Update('Вы подошли к рычагу.')
            if self.lever_state:
                window['-OUT-'].Update('Рычаг заклинило')
            else:
                window['-IMG-'].Update('img/lever.png')
                action = sg.PopupYesNo('Вы хотите нажать на рычаг?')
                if action == 'No':
                    window['-OUT-'].Update('Вы решили не рисковать')
                if action == 'Yes':
                    window['-OUT-'].Update('Вы дернули рычаг и услышали звук механизма. Но откуда шел звук?')
                    self.lever_state = True

        if event == 'Дверь':
            if self.lever_state:
                action = sg.PopupYesNo('Вы хотите зайти?')
                if action == 'Yes':
                    window['-OUT-'].Update('Вы вышли')
                    window.close()
            if not self.lever_state:
                window['-OUT-'].Update('Дверь закрыта')

if __name__ == '__main__':
    from enemy import Goblin, Rat

    pal = Paladin()
    gob = Goblin()
    pal.weapons = ['asdf', 'sdfgs', '1231', 'sdgfsg']
    test_room = Room1(pal)
    test_room.show()
