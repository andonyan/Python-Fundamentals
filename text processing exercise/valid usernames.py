input_string = input().split(', ')
output_list = []
for username in input_string:
    if 3 <= len(username) <= 16:
        for char in username:
            if char.isdigit() or char.isalpha() or char == '-' or char == '_':
                continue
            else:
                break
        else:
            output_list.append(username)

for string in output_list:
    print(string)