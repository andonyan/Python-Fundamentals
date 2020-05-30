def password_is_valid(string):
    if len(string) < 6 or len(string) >10:
        print('Password must be between 6 and 10 characters')
    number_of_digits = 0
    valid_string = True
    for char in string:
        if 49 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 121:
            if 49 <= ord(char) <= 57:
                number_of_digits += 1
        else:
            print('Password must consist only of letters and digits')
            valid_string = False
            break
    if number_of_digits < 2:
        print('Password must have at least 2 digits')
    return 6 <= len(string) <= 10 and valid_string and number_of_digits >= 2


a = input()
if password_is_valid(a):
    print('Password is valid')