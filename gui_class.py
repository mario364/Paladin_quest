import PySimpleGUI as sg

from hero import Paladin


class Window:

    def __init__(self, player, ways, title_room):
        self.player = player
        self.ways = ways
        self.title_room = title_room

    def setup(self):
        buttons = self.generate_button()  # Из списка событий генерируются кнопки.
        down_panel = self.generate_down_panel()  # Генерируются нижняя панель
        down_panel[0].append(sg.Frame('Действия', buttons))  # К нижней панели добавляются кнопки
        layout = [
            [sg.Column([[sg.Image(source='img/room.png', key='-IMG-')]]),  # В source передавай путь к файлу
             sg.Output(key='-OUT-', size=(30, 1), expand_y=True, font=16)],
            [sg.Column(down_panel, element_justification='center')]
        ]
        window = sg.Window(self.title_room, layout=layout,
                           element_justification='center')  # Создаем объект окна приложения
        return window

    @staticmethod
    def main_loop(window):
        while True:  # Главный цикл окна
            event, value = window.read()  # Считываются нажатия на кнопки
            if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
                break

    def generate_down_panel(self):
        player = self.player
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

    def generate_button(self):
        events = self.ways

        buttons = [
            [sg.Button(event) for event in events if events.index(event) % 2 == 0],
            [sg.Button(event) for event in events if events.index(event) % 2 == 1],
        ]
        return buttons

    def show(self):
        window = self.setup()
        self.main_loop(window)


class Inventory:
    def __init__(self, main_window, player):
        self.title = 'title'
        self.items = player.weapons
        self.main_window = main_window
        self.player = player

    def setup(self):
        buttons = [
            [sg.Button(item, key=self.items.index(item)) for item in self.items if self.items.index(item) % 3 == 0],
            [sg.Button(item, key=self.items.index(item)) for item in self.items if self.items.index(item) % 3 == 1],
            [sg.Button(item, key=self.items.index(item)) for item in self.items if self.items.index(item) % 3 == 2]
        ]

        layout = [[sg.Frame(self.title, buttons)]]
        window = sg.Window('Инвентарь', layout)
        return window

    @staticmethod
    def main_loop(window, main_window, player):
        pass

    def show(self):
        window = self.setup()
        self.main_loop(window, self.main_window, self.player)


class WeaponInventory(Inventory):

    def __init__(self, main_window, player):
        super().__init__(main_window, player)
        self.items = player.weapons
        self.title = 'Оружие'

    @staticmethod
    def main_loop(window, main_window, player):
        while True:  # Главный цикл окна
            event, value = window.read()  # Считываются нажатия на кнопки
            if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
                break
            player.equip(event)
            main_window['-WEAPON-'].Update(f'Оружие в руках: {player.weapon}')
            window.close()


class SpellsInventory(Inventory):

    def __init__(self, main_window, player):
        super().__init__(main_window, player)
        self.items = player.spells
        self.title = 'Заклинания'

    @staticmethod
    def main_loop(window, main_window, player):
        while True:  # Главный цикл окна
            event, value = window.read()  # Считываются нажатия на кнопки
            if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
                break
            player.equip_spell(event)
            main_window['-SPELL-'].Update(f'Активное заклинание: {player.spell}')
            window.close()


class Fight(Window):
    @staticmethod
    def main_loop(window):
        pass


pal = Paladin()
pal.weapons = ['asdf', 'sdfgs', '1231', 'sdgfsg']
