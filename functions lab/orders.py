def calculate_total_price(product, quantity):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'coke':
        return quantity * 1.4
    elif product == 'water':
        return  quantity * 1.0
    elif product == 'snacks':
        return quantity * 2.0


order = input()
amount = int(input())
print(f'{calculate_total_price(order, amount):.2f}')