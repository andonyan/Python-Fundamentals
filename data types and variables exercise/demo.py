initial_loot = input()

list_initial_loot = initial_loot.split("|")

stolen = []

command = input()
while command != "Yohoho!":
    tokens = command.split(" ")
    comanda = tokens[0]
    if comanda == "Loot":
        for k in tokens:
            if k not in list_initial_loot:
                if k != 'Loot':
                    list_initial_loot.insert(0, k)
    elif comanda == "Drop":
        index = int(tokens[1])
        if 0 < index < len(list_initial_loot):
            list_initial_loot.append(list_initial_loot[index])
            del list_initial_loot[index]
    elif comanda == "Steal":
        counta = int(tokens[1])
        stolen = []
        if 0 < counta < len(list_initial_loot):
            for i in range(0, counta):
                stolen.append(list_initial_loot[-1])
                del list_initial_loot[-1]
            stolen = stolen[::-1]
            print(", ".join(stolen))
        elif counta >= len(list_initial_loot):
            print(", ".join(list_initial_loot))
            list_initial_loot.clear()
    command = input()

if len(list_initial_loot) > 0:
    sum_of_items = 0

    for g in range(len(list_initial_loot)):
        sum_of_items += len(list_initial_loot[g])

    averageGain = sum_of_items / len(list_initial_loot)
    print(f"Average treasure gain: {averageGain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
