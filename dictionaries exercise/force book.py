users = {}

while True:
    input_string = input()
    if '|' in input_string:
        tokens = input_string.split(' | ')
        side = tokens[0]
        user = tokens[1]
        if users:
            for values in users.values():
                if user not in values:
                    if side not in users:
                        users[side] = [user]
                        break
                    else:
                        users[side].append(user)
                        break
        else:
            users[side] = [user]
    elif '->' in input_string:
        tokens = input_string.split(' -> ')
        user = tokens[0]
        side = tokens[1]
        for key, value in users.items():
            if user in value and key != side:
                users[key].remove(user)
                if len(users[key]) == 0:
                    del users[key]
                if side in users:
                    users[side].append(user)
                else:
                    users[side] = [user]
                print(f'{user} joins the {side} side!')
                break
        else:
            if side in users:
                #if user not in users[side]:
                users[side].append(user)
                print(f'{user} joins the {side} side!')
            else:
                users[side] = [user]
                print(f'{user} joins the {side} side!')
    else:
        output_users = {k: users[k] for k in users.keys() if len(users[k]) > 0}
        for key, value in sorted(output_users.items(), key=lambda x: (-len(x[1]), x[0])):
            print(f'Side: {key}, Members: {len(value)}')
            for usr in sorted(value):
                print(f'! {usr}')
        break
