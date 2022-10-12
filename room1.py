from gui_class import sg, Window, Fight
from hero import Paladin
from enemy import Rat, Goblin
from weapons import Sword
import random

class Room1(Window):
    lever_state = False
    ways = ["Сундук", "Рычаг", "Дверь"]
    title_room = 'Комната 1'
    start_message = 'Вы вошли в первую комнату'
    # rat = Rat()
    rat = Goblin()
    sword = Sword()
    chest_state = False
    # chest_stuff = [None, sword, rat]
    chest_stuff = [ rat]

    def main_loop(self, window, event, value):
        if event == 'Сундук':
            window['-IMG-'].Update('img/Chest.png')
            stuff = random.choice(self.chest_stuff)
            if self.chest_state:
                window['-OUT-'].Update('Сундук открыт и пуст')
            else:
                if not stuff:
                    window['-OUT-'].Update("В сундуке пусто")
                if stuff == self.sword:
                    window['-OUT-'].Update("Вы нашли меч")
                    self.player.weapons.append(self.sword)
                if stuff == self.rat:
                    sg.Popup('В сундуке была крыса!')
                    Fight(self.player, self.rat).show()
                self.chest_state = True

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

pal = Paladin()
pal.spells = ['asdf', 'asdfer']
test_room = Room1(pal)
test_room.show()