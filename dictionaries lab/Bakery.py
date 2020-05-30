my_dictionary = {}
input_list = input().split()

for i in range(0, len(input_list), 2):
    my_dictionary[input_list[i]] = int(input_list[i + 1])

print(my_dictionary)
