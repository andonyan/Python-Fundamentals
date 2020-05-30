first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))
rows = list(zip(first_row, second_row, third_row))
diagonals = [first_row[:1] + second_row[1:2] + third_row[2:], first_row[2:] + second_row[1:2] + third_row[0:1]]

if len(first_row) == first_row.count(1) or len(second_row) == second_row.count(1) or len(third_row) == third_row.count(
        1):
    print('First player won')
elif len(first_row) == first_row.count(2) or len(second_row) == second_row.count(2) or len(
        third_row) == third_row.count(2):
    print('Second player won')
elif len(rows[0]) == rows[0].count(1) or len(rows[1]) == rows[1].count(1) or len(rows[2]) == rows[2].count(1):
    print('First player won')
elif len(rows[0]) == rows[0].count(2) or len(rows[1]) == rows[1].count(2) or len(rows[2]) == rows[2].count(2):
    print('Second player won')
elif len(diagonals[0]) == diagonals[0].count(1) or len(diagonals[1]) == diagonals[1].count(1):
    print('First player won')
elif len(diagonals[0]) == diagonals[0].count(2) or len(diagonals[1]) == diagonals[1].count(2):
    print('Second player won')
else:
    print('Draw!')