force_book = {}

while True:
    input_string = input()

    if '|' in input_string:
        args = input_string.split(' | ')
        side = args[0]
        user = args[1]

        if not force_book:
            force_book[side] = [user]
        else:
            all_users = [item for current_list in force_book.values() for item in current_list]
            if user not in all_users:
                if side in force_book:
                    force_book[side].append(user)
                else:
                    force_book[side] = [user]
            else:
                continue

    elif '->' in input_string:
        args = input_string.split(' -> ')
        side = args[1]
        user = args[0]

        for key, value in force_book.items():
            if user in value:
                force_book[key].remove(user)
                if side in force_book:

                    force_book[side].append(user)
                    print(f'{user} joins the {side} side!')
                    break
                else:

                    force_book[side] = [user]
                    print(f'{user} joins the {side} side!')
                    break
        else:
            if side in force_book:
                force_book[side].append(user)
                print(f'{user} joins the {side} side!')
            else:
                force_book[side] = [user]
                print(f'{user} joins the {side} side!')

    else:
        output_users = {k: force_book[k] for k in force_book.keys() if len(force_book[k]) > 0}
        for key, value in sorted(output_users.items(), key=lambda x: (-len(x[1]), x[0])):
            print(f'Side: {key}, Members: {len(value)}')
            for usr in sorted(value):
                print(f'! {usr}')
        break
