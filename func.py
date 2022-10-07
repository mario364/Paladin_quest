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
    events = ["Ударить", "Сменить оружие", 'Колдовать', "Сбежать"]
    while True:
        action = get_action(events)
        if action == 1:
            if not player.weapon:
                print("У вас нет оружия в руках!")
                print('Доступное оружие: ')
                action = get_action(player.weapons, 'Оружие')
                player.equip(action - 1)
            damage = player.attack(enemy)
            print(f'Вы нанесли {damage} урона врагу')
            if enemy.hp <= 0:
                print('Вы победили!')
                break
            print(f"У врага осталось {enemy.hp} HP")
        if action == 2:
            player.equip()
            continue

        if action == 3:
            print('Выберите заклинание')
            action = get_action(player.spells, 'Заклинания')
            target = int(input(f'1 - {enemy}\n2 - {player}\nВыберите цель: '))
            if target == 1:
                target = enemy
            if target == 2:
                target = player
            player.wiz(action-1, target)

        damage = enemy.attack(player)
        print(f'Вам нанесли {damage} урона')
        if player.hp <= 0:
            print('Вы погибли!')
            break
        print(f'У вас осталось {player.hp} HP')

