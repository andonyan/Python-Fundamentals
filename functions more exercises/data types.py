def calculate(argument, value):
    if argument == 'string':
        return '$' + value + '$'
    elif argument == 'real':
        return f'{float(value) * 1.5:.2f}'
    elif argument == 'int':
        return f'{int(value) * 2}'


command = input()
variable = input()
print(calculate(command, variable))

