input_list = list(map(int, input().split()))
step = int(input())
output_list = []
current_index = step - 1
while len(input_list) > 0:
    output_list.append(input_list.pop(current_index))
    if len(input_list) > 0:
        current_index = (current_index + step - 1) % len(input_list)
print('[', end='')
print(",".join(map(str, output_list)), end='')
print(']', end='')