input_list = list(map(int, input().split()))
step = int(input())
output_list = []
if step - 1 < len(input_list):
    current_index = step - 1
    while len(input_list) > 0:
        output_list.append(input_list.pop(current_index))
        if len(input_list) > 0:
            current_index = (current_index + step - 1) % len(input_list)
elif step - 1 >= len(input_list):
    current_index = 0
    while len(input_list) > 0:
        output_list.append(input_list.pop((current_index + (step - 1)) % len(input_list)))
        if len(input_list) > 0:
            current_index = (current_index + (step - 1)) % (len(input_list) + 1)

print('[', end='')
print(",".join(map(str, output_list)), end='')
print(']', end='')