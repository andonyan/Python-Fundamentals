input_list = input().split()
totals = []
for string in input_list:
    first_letter = string[0]
    last_letter = string[-1]
    total_sum = 0
    digits = ''
    for digit in string[1:-1]:
        digits += digit
    number = int(digits)

    if first_letter.isupper():
        total_sum = number / (ord(first_letter) - 64)
    elif first_letter.islower():
        total_sum = number * (ord(first_letter) - 96)

    if last_letter.isupper():
        total_sum -= (ord(last_letter) - 64)
    elif last_letter.islower():
        total_sum += (ord(last_letter) - 96)

    totals.append(total_sum)

print(f'{sum(totals):.2f}')

