n = int(input())
ascii_sum = 0

for counter in range(n):
    i = input()
    ascii_sum += ord(i)

print(f'The sum equals: {ascii_sum}')

