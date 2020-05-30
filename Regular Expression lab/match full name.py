import re

regex = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'

text = input()
matches = re.findall(regex, text)
print(' '.join(matches))
