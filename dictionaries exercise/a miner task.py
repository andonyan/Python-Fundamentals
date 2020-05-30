my_dictionary = {}

while True:
    command = input()
    if command == 'stop':
        break
    else:
        value = int(input())
        if command in my_dictionary:
            my_dictionary[command] += value
        else:
            my_dictionary[command] = value

for key, value in my_dictionary.items():
    print(f'{key} -> {value}')