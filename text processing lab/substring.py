removal_string = input()
input_string = input()

while removal_string in input_string:
    input_string = input_string.replace(removal_string, '')

print(input_string)
