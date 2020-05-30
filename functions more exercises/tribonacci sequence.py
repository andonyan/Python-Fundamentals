def tribonacci(num):
    if num < 3:
        return tribonacci(num - 1) + tribonacci(num - 2) + tribonacci(num - 3)
    elif num == 3:
        return 2
    else:
        return 1



iterations = int(input())
for i in range(1, iterations + 1):
    # print(tribonacci(i), ' ')
    print(tribonacci(i), end=' ')
