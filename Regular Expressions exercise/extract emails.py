import re
text = input()

pattern = r'((?<=\s)[A-Za-z0-9]+([\.\-_]?[A-Za-z0-9]+)*@[A-Za-z0-9]+([\.\-_]?[A-Za-z0-9]+)*\.[A-Za-z0-9]+([\.\-_]?[A-Za-z0-9]+)*)'
for match in re.findall(pattern, text):
    print(match[0])


