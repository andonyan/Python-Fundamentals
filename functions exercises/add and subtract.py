def add_and_subtract(num1, num2, num3):
    def sum_numbers(inner_num1, inner_num2):
        return inner_num1 + inner_num2

    def subtract(int_argument, third_number):
        return int_argument - third_number

    return subtract(sum_numbers(num1, num2), num3)


a = int(input())
b = int(input())
c = int(input())
print(add_and_subtract(a, b, c))
