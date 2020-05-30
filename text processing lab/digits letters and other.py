input_string = input()
digits = ''
letters = ''
other = ''

for char in input_string:
    if char.isalpha():
        letters += char
    elif char.isdecimal():
        digits += char
    else:
        other += char

print(digits)
print(letters)
print(other)