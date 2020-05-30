input_string = list(map(int, input().split(', ')))
output_string = []
zeroes_required = 0
for item in input_string:
    if item != 0:
        output_string.append(item)
    else:
        zeroes_required += 1
for i in range(zeroes_required):
    output_string.append(0)
print(output_string)
