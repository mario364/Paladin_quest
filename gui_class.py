import PySimpleGUI as sg
from hero import Paladin


class Window:
    title_room = 'Заголовок'
    ways = ('Ты', 'Забыл', 'Указать', 'Варианты', 'Кнопок')
    img = 'img/start.png'
    _print_ = False
    start_message = '\nТекст для заполнения, вы не указали в дочернем классе переменную start_message'

    def __init__(self, player):
        self.player = player
        self.buttons = self.generate_button()
        self.down_panel = self.generate_down_panel()

    def setup(self):
        layout = self.generate_layout()
        window = sg.Window(self.title_room, layout=layout, element_justification='center')
        return window

    def main_loop(self, window, event, value):
        pass

    def generate_layout(self):
        output = sg.Column([[sg.Text(self.start_message, key='-OUT-', size=(35, 10), font=16,
                                     relief='groove', border_width=5, justification='center')]])
        if self._print_:
            output = sg.Output(size=(30, 1), expand_y=True, font=16)
        layout = [
            [sg.Column([[sg.Image(source=self.img, key='-IMG-')]]),  # В source передавай путь к файлу
             output],
            [sg.Column(self.down_panel, element_justification='center')]
        ]
        return layout

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
             sg.Frame('Действия', self.buttons)
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

    def start_loop(self, window):
        while True:  # Главный цикл окна
            event, value = window.read()  # Считываются нажатия на кнопки
            if event == sg.WINDOW_CLOSED:  # Реакция на нажатие крестика
                break
            if event == '-INV_WEAPONS-':
                WeaponInventory(window, self.player).show()
            if event == '-INV_SPELLS-':
                SpellsInventory(window, self.player).show()
            self.main_loop(window, event, value)
            window['-HP-'].Update(f'Здоровье: {self.player.hp} / {self.player.max_hp}')

    def show(self):
        window = self.setup()
        self.start_loop(window)


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
    title_room = 'Битва'
    ways = ["Ударить", "Колдовать", "Сбежать"]
    _print_ = True

    def __init__(self, player, enemy):
        super().__init__(player)
        self.enemy = enemy
        self.extend_down_panel()
        self.img = enemy.img

    def extend_down_panel(self):
        frame_enemy_feature = [
            [sg.Text(f'Здоровье: {self.enemy.hp} / {self.enemy.max_hp}', key='-HP_ENEMY-')],
        ]
        self.down_panel[0].append(sg.Frame(self.enemy, frame_enemy_feature))

    def main_loop(self, window, event, value):
        if event == 'Ударить':
            damage = self.player.attack(self.enemy)
            window['-HP_ENEMY-'].Update(f'Здоровье: {self.enemy.hp} / {self.enemy.max_hp}')
            print(f'Вы нанесли {damage} урона врагу')
            if self.enemy.hp <= 0:
                sg.Popup('Вы победили!')
                self.get_loot()
                window.close()
            damage = self.enemy.attack(self.player)
            window['-HP-'].Update(f'Здоровье: {self.player.hp} / {self.player.max_hp}')
            print(f'Вам нанесли {damage} урона')
            if self.player.hp <= 0:
                print('Вы погибли!')
                sg.Popup('Вы погибли!')
                window.close()
        if event == 'Колдовать':
            pass

        if event == 'Сбежать':
            pass

    def get_loot(self):
        loot = self.enemy.loot
        for stuff in loot:
            if stuff == 'gold':
                self.player.gold += loot[stuff]
            if stuff == 'weapon':
                self.player.weapons.append(loot[stuff])

if __name__ == '__main__':
    from enemy import Goblin, Rat
    pal = Paladin()
    gob = Goblin()
    pal.weapons = ['asdf', 'sdfgs', '1231', 'sdgfsg']

    Fight(pal, Rat()).show()
