def exchange_list(input_list, index):
    first_half = input_list[index + 1:]
    second_half = input_list[:index + 1]
    input_list.clear()
    if len(first_half) > 0:
        input_list.extend(first_half)
        input_list.extend(second_half)
    else:
        input_list.extend(second_half)

    return input_list


def min_max(input_list, extreme, parity):
    counter = 0
    current_extreme = 0
    index = 0
    if extreme == 'max' and parity == 'even':
        for j, i in enumerate(input_list):
            if i % 2 == 0 and counter == 0:
                current_extreme = i
                index = j
                counter += 1
            elif i % 2 == 0 and counter >= 0 and i >= current_extreme:
                current_extreme = i
                index = j
                counter += 1

        if counter > 0:
            print(f'{index}')
        else:
            print('No matches')


    elif extreme == 'max' and parity == 'odd':
        for j, i in enumerate(input_list):
            if i % 2 == 1 and counter == 0:
                current_extreme = i
                index = j
                counter += 1
            elif i % 2 == 1 and counter >= 0 and i >= current_extreme:
                current_extreme = i
                index = j
                counter += 1

        if counter > 0:
            print(f'{index}')
        else:
            print('No matches')

    elif extreme == 'min' and parity == 'even':
        for j, i in enumerate(input_list):
            if i % 2 == 0 and counter == 0:
                current_extreme = i
                index = j
                counter += 1
            elif i % 2 == 0 and counter >= 0 and i <= current_extreme:
                current_extreme = i
                index = j
                counter += 1

        if counter > 0:
            print(f'{index}')
        else:
            print('No matches')

    elif extreme == 'min' and parity == 'odd':
        for j, i in enumerate(input_list):
            if i % 2 == 1 and counter == 0:
                current_extreme = i
                index = j
                counter += 1
            elif i % 2 == 1 and counter >= 0 and i <= current_extreme:
                current_extreme = i
                index = j
                counter += 1

        if counter > 0:
            print(f'{index}')
        else:
            print('No matches')


def first(input_list, number_of_elements, parity):
    sliced = []
    if number_of_elements > len(input_list):
        print('Invalid count')
    else:
        if parity == 'even':
            for i in input_list:
                if i % 2 == 0 and len(sliced) < number_of_elements:
                    sliced.append(i)
            else:
                print(sliced)
        elif parity == 'odd':
            for i in input_list:
                if i % 2 == 1 and len(sliced) < number_of_elements:
                    sliced.append(i)
            else:
                print(sliced)


def last(input_list, number_of_elements, parity):
    sliced = []
    if number_of_elements > len(input_list):
        print('Invalid count')
    else:
        if parity == 'even':
            for i in input_list[::-1]:
                if i % 2 == 0 and len(sliced) < number_of_elements:
                    sliced.append(i)
            else:
                print(list(reversed(sliced)))
        elif parity == 'odd':
            for i in input_list[::-1]:
                if i % 2 == 1 and len(sliced) < number_of_elements:
                    sliced.append(i)
            else:
                print(list(reversed(sliced)))


input_array = list(map(int, input().split(' ')))

while True:
    command = input().split(' ')
    if command[0] == 'end':
        print(input_array)
        break
    else:
        if command[0] == 'exchange':
            if 0 <= int(command[1]) < len(input_array):
                exchange_list(input_array, int(command[1]))
            else:
                print('Invalid index')
        elif command[0] == 'max' or command[0] == 'min':
            min_max(input_array, command[0], command[1])
        elif command[0] == 'first':
            first(input_array, int(command[1]), command[2])
        elif command[0] == 'last':
            last(input_array, int(command[1]), command[2])
