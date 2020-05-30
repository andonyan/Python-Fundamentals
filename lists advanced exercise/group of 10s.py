input_numbers = list(map(int, input().split(', ')))
boundary = 0

while len(input_numbers) > 0:
    groups = []
    for number in input_numbers:
        if boundary <= number <= boundary + 10:
            groups.append(number)
    print(f'Group of {boundary + 10}\'s: {groups}')
    boundary += 10
    for number in groups:
        input_numbers.remove(number)



