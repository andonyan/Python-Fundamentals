string_list = input().split()

for string in string_list:
    print(string * len(string), end='')