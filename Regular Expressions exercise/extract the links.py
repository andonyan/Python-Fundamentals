import re

links = []
pattern = r'(www\.[A-Za-z0-9]+([-]?[A-Za-z0-9]+)*(\.[a-z]+)+)'

while True:
    text = input()
    if text:
        matches = re.findall(pattern, text)
        if matches:
            for match in matches:
                links.append(match[0])
        else:
            continue
    else:
        for link in links:
            print(link)
        break
