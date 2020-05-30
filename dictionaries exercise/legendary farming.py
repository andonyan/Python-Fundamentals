inventory = {'shards': 0, 'fragments': 0, 'motes': 0}
keep_going = True
while keep_going:
    tokens = input().lower().split()
    for i in range(0, len(tokens), 2):
        value = int(tokens[i])
        key = tokens[i + 1]
        if key in inventory:
            inventory[key] += value
            if key == 'shards' and inventory[key] >= 250:
                inventory[key] -= 250
                keep_going = False
                print('Shadowmourne obtained!')
                key_materials = {k: inventory[k] for k in ['shards', 'fragments', 'motes']}
                for k, v in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
                    print(f'{k}: {v}')
                junk = {m: inventory[m] for m in inventory.keys() if m not in ['shards', 'fragments', 'motes']}
                if junk:
                    for k, v in sorted(junk.items(), key=lambda x: (x[0])):
                        print(f'{k}: {v}')
                break
            elif key == 'fragments' and inventory[key] >= 250:
                inventory[key] -= 250
                keep_going = False
                print('Valanyr obtained!')
                key_materials = {k: inventory[k] for k in ['shards', 'fragments', 'motes']}
                for k, v in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
                    print(f'{k}: {v}')
                junk = {m: inventory[m] for m in inventory.keys() if m not in ['shards', 'fragments', 'motes']}
                if junk:
                    for k, v in sorted(junk.items(), key=lambda x: (x[0])):
                        print(f'{k}: {v}')
                break
            elif key == 'motes' and inventory[key] >= 250:
                inventory[key] -= 250
                keep_going = False
                print('Dragonwrath obtained!')
                key_materials = {k: inventory[k] for k in ['shards', 'fragments', 'motes']}
                for k, v in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
                    print(f'{k}: {v}')
                junk = {m: inventory[m] for m in inventory.keys() if m not in ['shards', 'fragments', 'motes']}
                if junk:
                    for k, v in sorted(junk.items(), key=lambda x: (x[0])):
                        print(f'{k}: {v}')
                break
        else:
            inventory[key] = value
            if key == 'shards' and inventory[key] >= 250:
                inventory[key] -= 250
                keep_going = False
                print('Shadowmourne obtained!')
                key_materials = {k: inventory[k] for k in ['shards', 'fragments', 'motes']}
                for k, v in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
                    print(f'{k}: {v}')
                junk = {m: inventory[m] for m in inventory.keys() if m not in ['shards', 'fragments', 'motes']}
                if junk:
                    for k, v in sorted(junk.items(), key=lambda x: (x[0])):
                        print(f'{k}: {v}')
                break
            elif key == 'fragments' and inventory[key] >= 250:
                inventory[key] -= 250
                keep_going = False
                print('Valanyr obtained!')
                key_materials = {k: inventory[k] for k in ['shards', 'fragments', 'motes']}
                for k, v in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
                    print(f'{k}: {v}')
                junk = {m: inventory[m] for m in inventory.keys() if m not in ['shards', 'fragments', 'motes']}
                if junk:
                    for k, v in sorted(junk.items(), key=lambda x: (x[0])):
                        print(f'{k}: {v}')
                break
            elif key == 'motes' and inventory[key] >= 250:
                inventory[key] -= 250
                keep_going = False
                print('Dragonwrath obtained!')
                key_materials = {k: inventory[k] for k in ['shards', 'fragments', 'motes']}
                for k, v in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
                    print(f'{k}: {v}')
                junk = {m: inventory[m] for m in inventory.keys() if m not in ['shards', 'fragments', 'motes']}
                if junk:
                    for k, v in sorted(junk.items(), key=lambda x: (x[0])):
                        print(f'{k}: {v}')
                break
