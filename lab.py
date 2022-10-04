from hero import Paladin
from enemy import Goblin
from func import fight

pal = Paladin()
gob = Goblin()

pal.weapon = pal.weapons[0]
fight(pal, gob)