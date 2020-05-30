input_string = input().replace(' ', '')
my_dictionary = {}
for char in input_string:
    if char in my_dictionary:
        my_dictionary[char] += 1
    else:
        my_dictionary[char] = 1

for k, v in my_dictionary.items():
    print(f'{k} -> {v}')
