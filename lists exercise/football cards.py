card_list = input().split()

team_a = [i for i in range(1, 12)]
team_b = [i for i in range(1, 12)]

for card in card_list:
    if card[0:1] == 'A' and int(card.split('-')[-1]) in team_a:
        team_a.remove(int(card.split('-')[-1]))
    elif card[0:1] == 'A' and int(card.split('-')[-1]) not in team_a:
        continue
    elif card[0:1] == 'B' and int(card.split('-')[-1]) in team_b:
        team_b.remove(int(card.split('-')[-1]))
    elif card[0:1] == 'B' and int(card.split('-')[-1]) not in team_b:
        continue



print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if len(team_a) < 7 or len(team_b) < 7:
    print(f'Game was terminated')
