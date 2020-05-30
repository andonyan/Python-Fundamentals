import re

regex = r'\b(\d{2})([./-])([A-Z]{1}[a-z]{2})\2(\d{4})\b'

input_string = input()
matches = re.findall(regex, input_string)

for match in matches:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')