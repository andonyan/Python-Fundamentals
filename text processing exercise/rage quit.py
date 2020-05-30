input_string = input()
unique_symbols = []
substring = []
output_string = ''


for i in range(len(input_string)):
    if not input_string[i].isdecimal():
        substring.append(input_string[i].upper())
        if input_string[i].upper() not in unique_symbols:
            unique_symbols.append(input_string[i].upper())

    else:
        m = i
        number = ''
        counter = 0
        while input_string[m].isdecimal():
            number += input_string[m]
            m += 1
            counter += 1
            if m == len(input_string):
                break
        #if counter > 1:
           # pass #print(input_string[i + 1: counter - 1])

        output_string += ''.join(substring) * int(number)
        substring.clear()

print(f'Unique symbols used: {len(unique_symbols)}')
print(output_string)
