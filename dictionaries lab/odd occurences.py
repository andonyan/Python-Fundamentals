input_string = list(map(lambda x: x.lower(), input().split()))
my_dictionary = {}
for item in input_string:
    if item in my_dictionary:
        my_dictionary[item] += 1
    else:
        my_dictionary[item] = 1

print(' '.join([item for item in my_dictionary if my_dictionary[item] % 2 != 0]))
