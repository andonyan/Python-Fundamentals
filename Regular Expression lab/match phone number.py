import re

regex = r'(\+359([-| ])2\2\d{3}\2\d{4}\b)'
string = input()

matches = re.findall(regex, string)
print(', '.join([phone for phone, sep in matches]))