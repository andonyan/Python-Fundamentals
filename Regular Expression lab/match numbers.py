import re

pattern = r'((^|(?<=\s))-?\d+(\.?\d+)?($|(?=\s)))'
input_string = input()

matches = re.finditer(pattern, input_string)

for match in matches:
    print(match.group(0), end=' ')
