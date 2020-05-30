def reverse_string(string):
    return string[::-1]


while True:
    input_string = input()
    if input_string == 'end':
        break
    else:
        print(f'{input_string} = {reverse_string(input_string)}')
