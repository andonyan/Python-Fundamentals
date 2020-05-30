num_list = []
num1 = float(input())
num_list.append(num1)
num2 = float(input())
num_list.append(num2)
num3 = float(input())
num_list.append(num3)
product_negative = False
counter = 0
for num in num_list:
    if num == 0:
        print('zero')
        break
    elif num < 0:
        if counter % 2 == 0:
            product_negative = True
            counter += 1
        else:
            product_negative = False
            counter += 1
else:
    if product_negative:
        print('negative')
    else:
        print('positive')
