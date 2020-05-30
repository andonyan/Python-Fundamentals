input_string = input().split('|')

for index, string in enumerate(input_string):
    new_string = string.split('->')
    input_string[index] = new_string

budget = float(input())
profit = 0
bought_items = []

for item, price in input_string:
    if item == 'Clothes' and float(price) <= 50 and budget >= float(price):
        budget -= float(price)
        profit += ((float(price) * 1.4) - float(price))
        bought_items.append(round(float(price) * 1.4, 2))
    elif item == 'Shoes' and float(price) <= 35 and budget >= float(price):
        budget -= float(price)
        profit += (float(price) * 1.4 - float(price))
        bought_items.append(round(float(price) * 1.4, 2))
    elif item == 'Accessories' and float(price) <= 20.5 and budget >= float(price):
        budget -= float(price)
        profit += (float(price) * 1.4 - float(price))
        bought_items.append(round(float(price) * 1.4, 2))


for item in bought_items:
    print(f'{item:.2f} ', end='')
print()
print(f'Profit: {profit:.2f}')
if budget + sum(bought_items) >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
