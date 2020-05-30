class Party:
    def __init__(self):
        self.guests = []



party = Party()
while True:
    name = input()
    if name == 'End':
        break
    else:
        party.guests.append(name)

going = ", ".join(party.guests)
print(f'Going: {going}')
print(f'Total: {len(party.guests)}')
