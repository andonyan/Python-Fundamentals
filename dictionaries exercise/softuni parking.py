park_registry = {}
commands_count = int(input())

for i in range(commands_count):
    tokens = input().split()
    if tokens[0] == 'register':
        username = tokens[1]
        licence_plate = tokens[2]
        # could need a check if username & same licence plate already exist
        if username in park_registry:
            print(f'ERROR: already registered with plate number {park_registry[username]}')
        else:
            print(f'{username} registered {licence_plate} successfully')
            park_registry[username] = licence_plate
    elif tokens[0] == 'unregister':
        username = tokens[1]
        if username not in park_registry:
            print(f'ERROR: user {username} not found')
        else:
            print(f'{username} unregistered successfully')
            del park_registry[username]
else:
    for k, v in park_registry.items():
        print(f'{k} => {v}')

