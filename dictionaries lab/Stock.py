tokens = input().split()
products = {tokens[i]: int(tokens[i + 1]) for i in range(0, len(tokens), 2)}
searched_products = input().split()
for item in searched_products:
    if item in products:
        print(f'We have {products[item]} of {item} left')
    else:
        print(f'Sorry, we don\'t have {item}')
