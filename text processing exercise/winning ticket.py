tickets = input()
tickets_list = tickets.replace(' ', '').split(',')

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets_list:

    if len(ticket) != 20:
        print('invalid ticket')
        continue

    else:
        left_half = ticket[0:10]
        right_half = ticket[10:20]
        left_half_match = False
        right_half_match = False
        match_symbol = ''
        match_length = 0
        match_length_left = 0
        match_length_right = 0

        for symbol in winning_symbols:
            if symbol in left_half:
                left_sequence = 0
                right_sequence = 0

                for char in left_half[left_half.index(symbol):]:
                    if char == symbol:
                        left_sequence += 1
                        if left_sequence >= 6:
                            match_length_left = left_sequence
                            left_half_match = True
                    else:
                        left_sequence = 0

                if left_half_match:
                    for char in right_half[right_half.index(symbol):]:
                        if char == symbol:
                            right_sequence += 1
                            if right_sequence >= 6:
                                match_length_right = right_sequence
                                right_half_match = True
                        else:
                            right_sequence = 0

                if left_half_match and right_half_match:
                    match_symbol = symbol
                    if match_length_left > match_length_right:
                        match_length = match_length_right
                    elif match_length_left < match_length_right:
                        match_length = match_length_left
                    elif match_length_left == match_length_right:
                        match_length = match_length_left

                    if 6 <= match_length <= 9:
                        print(f'ticket "{ticket}" - {match_length}{match_symbol}')
                    elif match_length == 10:
                        print(f'ticket "{ticket}" - {match_length}{match_symbol} Jackpot!')
                    break
        else:
            print(f'ticket "{ticket}" - no match')
