from gui_class import sg, Window, Fight
from hero import Paladin
from enemy import Goblin


class Room2(Window):
    title_room = 'Комната 1'
    ways = ["Пойти на звук", "Пойти к книге", "Пойти к двери"]
    start_message = '\nВы вошли в первую комнату'
    img = 'img/room.png'
    door_state = False
    irdis_state = True
    bible_state = True
    gob = Goblin()

    def main_loop(self, window, event, value):
        if event == 'Пойти на звук':
            if self.irdis_state:
                window['-IMG-'].Update('img/zicon2.5.png')
                window['-OUT-'].Update('Вы увидели умирающего старца на которого нападает гоблин')
                action = sg.PopupYesNo('Вы хотите помочь?')
                if action == 'No':
                    window['-OUT-'].Update('Вы ушли, бросив старца умирать. Разве паладины так поступают?..')
                if action == 'Yes':
                    window['-OUT-'].Update('Вы вступили в бой с гоблином!')
                    Fight(self.player, self.gob)
                    if self.player.hp < 0:
                        sg.Popup('Вы проиграли')
                        return "Вы проиграли!"
                    if self.gob.hp < 0:
                        window['-OUT-'].Update('Спасибо, паладин! Дверь из этой комнаты можно открыть только '
                                               'если правильно постучать! Старец дал вам код')
                        self.door_state = True
                        window['-OUT-'].Update('За помощь, я излечу твои раны =)')
                        self.player.hp = self.player.max_hp
                self.irdis_state = False
            if not self.irdis_state:
                window['-OUT-'].Update('Старика больше нет.')

        if event == 'Пойти к книге':
            if self.bible_state:
                action = sg.PopupYesNo('Вы хотите прочитать?')
                if action == 'Yes':
                    window['-OUT-'].Update('Вы прочли книгу и расшифровали код от двери')
                    self.door_state = True
                if action == 'No':
                    window['-OUT-'].Update('Вы не прочитали книгу')
                    self.door_state = False
            if not self.bible_state:
                window['-OUT-'].Update('Вы уже прочли книгу')


        if event == 'Пойти к двери':
            if self.door_state == False:
                window['-OUT-'].Update("Дверь закрыта")
            if self.door_state == True:
                window['-OUT-'].Update('Вы вошли в дверь')


pal = Paladin()
Room2(pal).show()
