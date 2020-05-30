animals = {}
areas = {}

while True:
    tokens = input().split(':')
    if tokens[0] == 'Last Info':
        break
    else:
        command = tokens[0]
        animal_name = tokens[1]
        food = int(tokens[2])
        area = tokens[3]
        if command == 'Add':
            if animal_name not in animals:
                animals[animal_name] = food
                if area not in areas:
                    areas[area] = 1
                else:
                    areas[area] += 1
            else:
                animals[animal_name] += food

        else:
            if animal_name in animals:
                animals[animal_name] -= food
                if animals[animal_name] <= 0:
                    print(f'{animal_name} was successfully fed')
                    del animals[animal_name]
                    areas[area] -= 1
                    if areas[area] <= 0:
                        del areas[area]
animals_sorted = sorted(sorted(animals.items(), key=lambda a: a[0]), key=lambda b: b[1], reverse=True)
areas_sorted = sorted(areas.items(), key=lambda c: c[1], reverse=True)
print('Animals:')
for item in animals_sorted:
    print(f'{item[0]} -> {item[1]}g')
print('Areas with hungry animals:')
for item in areas_sorted:
    print(f'{item[0]} : {item[1]}')
