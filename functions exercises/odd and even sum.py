def odd_and_even(a):
    odd_sum = 0
    even_sum = 0
    for digit in a:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    output_string = f'Odd sum = {odd_sum}, Even sum = {even_sum}'
    return output_string


number = input()
print(odd_and_even(number))
