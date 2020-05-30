stores = {}

while True:
    tokens = input().split('->')
    if tokens[0] == 'END':
        break
    else:
        command = tokens[0]
        store = tokens[1]
        if command == 'Add':
            items = [item for item in tokens[2].split(',')]
            if store not in stores:
                stores[store] = items
            else:
                stores[store] += items

        else:
            if store in stores:
                del stores[store]

stores_sorted = sorted(stores.items(), key=lambda a: (len(a[1]), a[0]), reverse=True)
print('Stores list:')
for key, value in stores_sorted:
    print(f'{key}')
    for item in value:
        print(f'<<{item}>>')

