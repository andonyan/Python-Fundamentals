def converter(first_string, second_string):
    output_string = []
    for i in range(ord(first_string) + 1, ord(second_string)):
        output_string.append(chr(i))
    return ' '.join(output_string)


a = input()
b = input()
print(converter(a, b))
