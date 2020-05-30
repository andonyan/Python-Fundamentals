def factorial_division(n):
    if n > 1:
        return n * factorial_division(n - 1)
    else:
        return 1


a = int(input())
b = int(input())
print(f'{factorial_division(a) / factorial_division(b):.2f}')
