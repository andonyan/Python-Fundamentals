offers = input().split(', ')
beggars = int(input())
i = 0
output_list = []

if beggars < len(offers):
    new_list = []
    while i < beggars:
        for m in range(i, len(offers), beggars):
            new_list.append(int(offers[m]))
        i += 1
        output_list.append(sum(new_list))
        new_list.clear()
elif beggars == len(offers):
    output_list = list(map(int, offers))
else:

    new_beggar_count = beggars - len(offers)
    output_list = list(map(int, offers))
    for _ in range(new_beggar_count):
        output_list.append(0)
print(output_list)




