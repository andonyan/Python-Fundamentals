starting_index = int(input())
ending_index = int(input())

for counter in range(starting_index, ending_index + 1):
    print(f'{chr(counter)} ', end='')
