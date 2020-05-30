products = {}

while True:
    tokens = input().split()
    if tokens[0] == 'buy':
        for k, v in products.items():
            print(f'{k} -> {v[0] * v[1]:.2f}')
        break
    else:
        product = tokens[0]
        price = float(tokens[1])
        quantity = int(tokens[2])
        if product in products:
            products[product][1] += quantity
            if products[product][0] != price:
                products[product][0] = price
        else:
            products[product] = [price, quantity]
