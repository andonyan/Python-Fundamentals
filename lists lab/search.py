n = int(input())
word=input()
strings = []
for _ in range(n):
    strings.append(input())
print(strings)
for i in range(len(strings) - 1, 0, -1):
    if word not in strings[i]:
        strings.remove(strings[i])
print(strings)







