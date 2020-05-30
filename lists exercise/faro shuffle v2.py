string = list(map(str, input().split()))
shuffles_num = int(input())
first_part = []
second_part = []
for i in range(shuffles_num):
    first_part, second_part = string[::2], string[1::2]
    string.clear()
    for x in range(len(first_part)):
        string.append(first_part[x])
        string.append(second_part[x])

print(string)