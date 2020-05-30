import re

pattern = r'^>>[A-Za-z]+<<[0-9]+(\.[0-9]+)?![0-9]+$'
total_price = 0
furniture = []
while True:
    text = input()
    if text != 'Purchase':
        if re.search(pattern, text):
            tokens = re.split('>>|<<|!', text)
            item = tokens[1]
            price = float(tokens[2])
            quantity= int(tokens[3])
            furniture.append(item)
            total_price += price * quantity
        else:
            continue
    else:
        print('Bought furniture:')
        for item in furniture:
            print(item)
        print(f'Total money spend: {total_price:.2f}')
        break
