my_dictionary = {}
word_count = int(input())
for i in range(word_count):
    word = input()
    synonym = input()
    if word not in my_dictionary:
        my_dictionary[word] = [synonym]
    else:
        my_dictionary[word].append(synonym)

for key in my_dictionary:
    print(f'{key} - {", ".join(my_dictionary[key])}')