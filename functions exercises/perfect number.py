def is_perfect_number(number):
    divisors_sum = 0
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            divisors_sum += i

    return number == divisors_sum


#a = int(input())
#if is_perfect_number(a):
    #print('We have a perfect number!')
#else:
    #print('It\'s not so perfect.')

for t in range(1, 10000):
    if is_perfect_number(t):
        print(f'{t} is a magic number.')
