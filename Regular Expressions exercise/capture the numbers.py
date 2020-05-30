import re

strings = []
matches = []
while True:
    line = input()
    if line:
        strings.append(line)
    else:
        break

pattern = r'[0-9]+'
for string in strings:
    matches = re.findall(pattern, string)
    for match in matches:
        print(f'{match}', end=' ')
