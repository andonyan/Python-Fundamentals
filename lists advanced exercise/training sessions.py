roads = {}

while True:
    tokens = input().split('->')
    if tokens[0] == 'END':
        break
    else:
        command = tokens[0]
        if command == 'Add':
            road = tokens[1]
            racer = tokens[2]
            if road not in roads:
                roads[road] = []
                roads[road].append(racer)
            else:
                roads[road].append(racer)
        elif command == 'Move':
            current_road = tokens[1]
            current_racer = tokens[2]
            next_road = tokens[3]
            if current_racer in roads[current_road]:
                roads[next_road].append(current_racer)
                roads[current_road].remove(current_racer)
        else:
            if tokens[1] in roads:
                del roads[tokens[1]]

sorted_roads = sorted(roads.items(), key=lambda a: (a[0]))
sorted_roads = sorted(sorted_roads, key=lambda b: len(b[1]), reverse=True)
print('Practice sessions:')
for road, racers in sorted_roads:
    print(f'{road}')
    for racer in racers:
        print(f'++{racer}')

