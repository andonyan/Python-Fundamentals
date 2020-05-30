first_list = input().split(', ')
second_list = input().split(', ')
matches = []
for word in first_list:
    for string in second_list:
        if word in string:
            matches.append(word)
            break
print(matches)

