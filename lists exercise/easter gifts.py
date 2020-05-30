list_of_gifts = input().split()
command = ['']

while command[0] != 'No':
    command = input().split()
    if command[0] == 'OutOfStock':
        for i in range(len(list_of_gifts)):
            if list_of_gifts[i] == command[1]:
                list_of_gifts[i] = 'None'
    elif command[0] == 'Required':
        if 0 <= int(command[2]) < len(list_of_gifts):
            list_of_gifts[int(command[2])] = command[1]
    elif command[0] == 'JustInCase':
        list_of_gifts[-1] = command[1]

final_list = [i for i in list_of_gifts if i != 'None']
print(*final_list)