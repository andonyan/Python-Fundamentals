def is_palindrome(string):
    return string == ''.join(reversed(string))


input_list = input().split(', ')
for number in input_list:
    print(is_palindrome(number))
