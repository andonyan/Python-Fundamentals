n = int(input())

for first_counter in range(n):
    for second_counter in range(n):
        for third_counter in range(n):
            print(f'{chr(97 + first_counter)}{chr(97 + second_counter)}{chr(97 + third_counter)}')
