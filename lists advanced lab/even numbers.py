input_list = list(map(int, input().split(', ')))
even_indices = [i for i in range(len(input_list)) if input_list[i] % 2 == 0]
print(even_indices)