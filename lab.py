from armors_unit import Helmet
from hero import Paladin
from enemy import *
from old_code.func import *
from weapons import *


pal = Paladin()
rat = Rat(loot={'gold': 7, 'armor': Helmet()})
rat2 = Rat(loot={'gold': 10, 'weapon': Sword()})
gob = Goblin(loot={'gold': 35, 'weapon': Rare_sword()})
gob1 = Goblin(loot={'gold': 350})

print(f'{pal.hp=}\n{pal.max_hp=}\n{pal.exp=}\n{pal.max_exp=}\n{pal.gold=}\n{pal.armor=}')
for enemy in (rat2, gob, rat, gob1):
    fight(pal, enemy)
    print('+' * 20)
    print(f'{pal.hp=}\n{pal.max_hp=}\n{pal.exp=}\n{pal.max_exp=}\n{pal.gold=}\n{pal.armor=}')





