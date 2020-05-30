input_string = input()
my_list = list(map(int, input_string.split()))
for i in range(len(my_list)):
    my_list[i] *= -1
print(my_list)



