input_string = input().split()
total_sum = 0

if len(input_string[0]) > len(input_string[1]):
    for i in range(len(input_string[1])):
        total_sum += ord(input_string[0][i]) * ord(input_string[1][i])

    for char in input_string[0][-1:-(len(input_string[0]) - len(input_string[1]) + 1):-1]:
        total_sum += ord(char)

elif len(input_string[1]) > len(input_string[0]):
    for i in range(len(input_string[0])):
        total_sum += ord(input_string[0][i]) * ord(input_string[1][i])

    for char in input_string[1][-1:-(len(input_string[1]) - len(input_string[0]) + 1):-1]:
        total_sum += ord(char)

else:
    for i in range(len(input_string[0])):
        total_sum += ord(input_string[0][i]) * ord(input_string[1][i])

print(total_sum)
