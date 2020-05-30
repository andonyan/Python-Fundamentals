input_string = list(input())
output_string = ''

for i in range(len(input_string) - 2):
    if input_string[i] != input_string[i + 1]:
        output_string += input_string[i]

if input_string[len(input_string) - 2] == input_string[len(input_string) - 1]:
    output_string += input_string[-1]
else:
    output_string += input_string[-2] + input_string[-1]

print(output_string)