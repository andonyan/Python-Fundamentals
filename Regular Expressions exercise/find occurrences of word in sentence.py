import re

sentence = input()
string = input()

string = '\\b' + string + '\\b'
matches = re.findall(string, sentence, re.IGNORECASE)

print(len(matches))