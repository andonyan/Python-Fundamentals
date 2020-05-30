def find_palindromes(string_list, palindrome):
    found_palindromes = []
    palindrome_found = 0
    for string in string_list:
        if string == string[::-1]:
            found_palindromes.append(string)
            if string == palindrome:
                palindrome_found += 1
    print(found_palindromes)
    print(f'Found palindrome {palindrome_found} times')


input_string = input().split()
searched_palindrome = input()
find_palindromes(input_string, searched_palindrome)

