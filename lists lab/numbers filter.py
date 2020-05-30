n = int(input())
numbers = []
filtered_numbers = []
for _ in range(n):
    numbers.append(int(input()))
command = input()
if command == 'even':
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            filtered_numbers.append(numbers[i])
    print(filtered_numbers)
elif command == 'odd':
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            filtered_numbers.append(numbers[i])
    print(filtered_numbers)
elif command == 'negative':
    for i in range(len(numbers)):
        if numbers[i] < 0:
            filtered_numbers.append(numbers[i])
    print(filtered_numbers)
elif command == 'positive':
    for i in range(len(numbers)):
        if numbers[i] >= 0:
            filtered_numbers.append(numbers[i])
    print(filtered_numbers)


