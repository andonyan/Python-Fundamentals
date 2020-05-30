number_of_wagons = int(input())
trains = [0] * number_of_wagons

while True:
    command = input().split(' ')
    if command[0] == 'End':
        print(trains)
        break
    elif command[0] == 'add':
        trains[-1] += (int(command[1]))
    elif command[0] == 'insert':
        trains[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        trains[int(command[1])] -= int(command[2])
