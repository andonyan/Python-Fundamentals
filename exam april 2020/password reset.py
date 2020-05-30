initial_string = input()

while True:
    command = input().split()

    if command[0] != 'Done':
        if command[0] == 'TakeOdd':
            initial_string = initial_string[1::2]
            print(initial_string)

        elif command[0] == 'Cut':
            index = int(command[1])
            length = int(command[2])
            initial_string = initial_string[:index] + initial_string[index + length:]
            print(initial_string)

        elif command[0] == 'Substitute':
            substring = command[1]
            substitute = command[2]
            if substring in initial_string:
                initial_string = initial_string.replace(substring, substitute)
                print(initial_string)
            else:
                print('Nothing to replace!')

    else:
        print(f'Your password is: {initial_string}')
        break
