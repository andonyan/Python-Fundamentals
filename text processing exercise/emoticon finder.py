input_string = input()
output_list = []

for i in range(len(input_string)):
    if input_string[i] == ':':
        output_list.append(input_string[i] + input_string[i + 1])
else:
    for item in output_list:
        print(item)