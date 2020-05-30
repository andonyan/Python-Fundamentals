initial_energy = 100
initial_coins = 100
is_bankrupt = False
events = input().split('|')

for item in events:
    split_order = item.split('-')
    order = split_order[0]
    amount = split_order[1]
    if order == 'rest' and initial_energy + int(amount) <= 100:
        initial_energy += int(amount)
        print(f'You gained {int(amount)} energy.')
        print(f'Current energy: {initial_energy}.')
        continue
    elif order == 'rest' and initial_energy + int(amount) > 100:
        print(f'You gained {100 - initial_energy} energy.')
        initial_energy += (100 - initial_energy)
        print(f'Current energy: {initial_energy}.')
        continue
    elif order == 'order' and initial_energy >= 30:
        print(f'You earned {int(amount)} coins.')
        initial_coins += int(amount)
        initial_energy -= 30
        continue
    elif order == 'order' and initial_energy < 30:
        print('You had to rest!')
        initial_energy += 50
        continue
    else:
        if initial_coins - int(amount) > 0:
            initial_coins -= int(amount)
            print(f'You bought {order}.')
        else:
            print(f'Closed! Cannot afford {order}.')
            is_bankrupt = True
            break
if not is_bankrupt:
    print(f'Day completed!')
    print(f'Coins: {initial_coins}')
    print(f'Energy: {initial_energy}')
