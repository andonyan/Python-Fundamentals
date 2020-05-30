import re

pattern = r'@#+[A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1}@#+\s*$'

n = int(input())

for _ in range(n):
    barcode = input()
    product_group = ''
    if re.match(pattern, barcode):
        for char in barcode:
            if char.isdigit():
                product_group += char

        if product_group:
            print(f'Product group: {product_group}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
