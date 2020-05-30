input_string = input().split('#')
for i in range(len(input_string)):
    input_string[i] = input_string[i].split(' = ')
water_amount = int(input())
effort = 0
total_fire = 0
output_string = []
for type_of_fire, cell_number in input_string:
    if type_of_fire == 'High' and 81 <= int(cell_number) <= 125 and water_amount >= int(cell_number):
        water_amount -= int(cell_number)
        effort += int(cell_number) * 0.25
        total_fire += int(cell_number)
        output_string.append(type_of_fire)
        output_string.append(cell_number)
    elif type_of_fire == 'Medium' and 51 <= int(cell_number) <= 80 and water_amount >= int(cell_number):
        water_amount -= int(cell_number)
        effort += int(cell_number) * 0.25
        total_fire += int(cell_number)
        output_string.append(type_of_fire)
        output_string.append(cell_number)
    elif type_of_fire == 'Low' and 1 <= int(cell_number) <= 50 and water_amount >= int(cell_number):
        water_amount -= int(cell_number)
        effort += int(cell_number) * 0.25
        total_fire += int(cell_number)
        output_string.append(type_of_fire)
        output_string.append(cell_number)
    else:
        continue
print("Cells:")
for t in range(1, len(output_string), 2):
    print(f'- {int(output_string[t])}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
