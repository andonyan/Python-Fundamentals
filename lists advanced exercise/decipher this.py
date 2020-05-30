secret_message = input().split()

for word in secret_message:
    digits_converted = chr(int(''.join(filter(lambda i: i.isdigit(), word))))
    characters = ''.join(filter(lambda i: i.isalpha(), word))
    if len(characters) == 1:
        print(f'{digits_converted + characters}', end=' ')
    else:
        characters_swapped = characters[-1] + characters[1:len(characters) - 1] + characters[0]
        print(f'{digits_converted + characters_swapped}', end=' ')


