import re
text = input()
output_string = ''
regex = r'((?<=\s_)[0-9A-Za-z]+\b)'
matches = re.findall(regex, text)
print(','.join(matches))

