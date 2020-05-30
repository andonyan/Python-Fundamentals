products = {}

while True:
    tokens = input().split(': ')
    if tokens[0] == 'statistics':
        print('Products in stock:')
        for k, v in products.items():
            print(f'- {k}: {v}')
        print(f'Total Products: {len(products.keys())}')
        print(f'Total Quantity: {sum(products.values())}')
        break
    else:
        key = tokens[0]
        value = int(tokens[1])
        if key in products:
            products[key] += value
        else:
            products[key] = value

