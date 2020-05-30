n = int(input())
heroes = {}

for i in range(n):
    tokens = input().split()
    hero_name = tokens[0]
    hero_hitpoints = int(tokens[1])
    hero_manapoints = int(tokens[2])
    heroes[hero_name] = [hero_hitpoints, hero_manapoints]

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        for key, value in sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])):
            print(key)
            print(f'  HP: {value[0]}')
            print(f'  MP: {value[1]}')
        break

    else:
        if command[0] == 'CastSpell':
            name = command[1]
            required_mana = int(command[2])
            spell = command[3]

            if heroes[name][1] >= required_mana:
                print(f'{name} has successfully cast {spell} and now has {heroes[name][1] - required_mana} MP!')
                heroes[name][1] -= required_mana
            else:
                print(f'{name} does not have enough MP to cast {spell}!')

        elif command[0] == 'TakeDamage':
            name = command[1]
            damage = int(command[2])
            attacker = command[3]

            if heroes[name][0] - damage > 0:
                print(f'{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0] - damage} HP left!')
                heroes[name][0] -= damage
            else:
                print(f'{name} has been killed by {attacker}!')
                del heroes[name]

        elif command[0] == 'Recharge':
            name = command[1]
            amount = int(command[2])

            if heroes[name][1] + amount <= 200:
                print(f'{name} recharged for {amount} MP!')
                heroes[name][1] += amount
            else:
                print(f'{name} recharged for {200 - heroes[name][1]} MP!')
                heroes[name][1] = 200

        elif command[0] == 'Heal':
            name = command[1]
            amount = int(command[2])

            if heroes[name][0] + amount <= 100:
                print(f'{name} healed for {amount} HP!')
                heroes[name][0] += amount
            else:
                print(f'{name} healed for {100 - heroes[name][0]} HP!')
                heroes[name][0] = 100
