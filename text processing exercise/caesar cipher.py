input_string = input()
output_string = ''

for char in input_string:
    output_string += chr(ord(char) + 3)

print(output_string)