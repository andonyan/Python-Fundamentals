import math


def center_point(x_1, y_1, x_2, y_2):
    first_distance = math.sqrt(abs(x_1) ** 2 + abs(y_1) ** 2)
    second_distance = math.sqrt(abs(x_2) ** 2 + abs(y_2) ** 2)

    if first_distance == second_distance:
        return int(x_1), int(y_1)
    else:
        if first_distance > second_distance:
            return int(x_2), int(y_2)
        else:
            return int(x_1), int(y_1)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(center_point(x1, y1, x2, y2))
