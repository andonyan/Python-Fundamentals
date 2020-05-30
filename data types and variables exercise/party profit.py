party_size = int(input())
days_of_adventure = int(input())

gathered_coins = 0

for counter in range(1, days_of_adventure + 1):
    if counter % 10 == 0:
        party_size -= 2
    if counter % 15 == 0:
        party_size += 5

    gathered_coins += 50 - (party_size * 2)
    if counter % 3 == 0:
        gathered_coins -= party_size * 3
    if counter % 5 == 0 and counter % 3 != 0:
        gathered_coins += party_size * 20
    elif counter % 5 == 0 and counter % 3 == 0:
        gathered_coins += party_size * 20 - party_size * 2

print(f'{party_size} companions received {gathered_coins // party_size} coins each.')
