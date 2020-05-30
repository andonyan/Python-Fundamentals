input_list = input().split('>')
output_string = ''.join(input_list[0])
remainder = 0


for substring in input_list[1:]:
    if len(substring) == int(substring[0]):
        output_string += '>'

    elif len(substring) < int(substring[0]):
        output_string += '>'
        remainder = int(substring[0]) - len(substring)

    elif len(substring) > int(substring[0]):
        if remainder > 0:
            if remainder + int(substring[0]) <= len(substring):
                output_string += '>'
                output_string += substring[remainder + int(substring[0]):]
                remainder = 0
            else:
                output_string += '>'
        else:
            if int(substring[0]) <= len(substring):
                output_string += '>'

                output_string += substring[int(substring[0]):]
            else:
                output_string += '>'

print(output_string)
