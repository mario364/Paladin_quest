def get_action(events, title='Действия'):
    print(f' {title} '.center(21, '_'))
    for num, event in enumerate(events, 1):
        print('|', f'{num} {event}'.center(17), '|')
    print(''.center(21, '_'))
    action = int(input("Что сделать? "))
    return action

def fight(player, enemy):
    print('Вы вступили в бой!')
    print(f'У вас осталось {player.hp} HP')
    events = ["Ударить", "Сменить оружие", "Сбежать"]
    while True:
        action = get_action(events)
        if action == 1:
            if not player.weapon:
                print("У вас нет оружия в руках!")
                player.equip()
            damage = player.attack(enemy)
            print(f'Вы нанесли {damage} урона врагу')
            if enemy.hp <= 0:
                print('Вы победили!')
                break
            print(f"У врага осталось {enemy.hp} HP")
        if action == 2:
            player.equip()
            continue
        damage = enemy.attack(player)
        print(f'Вам нанесли {damage} урона')
        if player.hp <= 0:
            print('Вы погибли!')
            break
        print(f'У вас осталось {player.hp} HP')

