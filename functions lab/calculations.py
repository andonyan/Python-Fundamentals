def calc(a, b, operator):
    if operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    elif operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)


operation = input()
num1 = int(input())
num2 = int(input())
print(calc(num1, num2, operation))
