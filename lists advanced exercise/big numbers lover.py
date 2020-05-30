numbers = input().split(' ')
numbers.sort(reverse=True)
for number in numbers:
    print(number, end='')
