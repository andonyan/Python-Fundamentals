def tribonacci(num):
    first = 1
    second = 1
    third = 2
    print('1', end=' ')
    if num == 2:
        print('1', end=' ')
    elif num == 3:
        print('1 2', end=' ')
    elif num > 3:
        print('1 2', end=' ')
        for i in range(3, num):
            current = first + second + third
            first = second
            second = third
            third = current
            print(current, end=' ')


n = int(input())
tribonacci(n)
