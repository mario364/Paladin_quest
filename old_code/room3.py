from minions import Imp
from func import get_action


def room3():
    mirarel = True
    imp1 = Imp()
    ways = ["Налево", "Направо", "Вперед"]

    while True:
        action = get_action(ways)

        #if action == 1