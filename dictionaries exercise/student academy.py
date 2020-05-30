student_count = int(input())
grades = {}

for _ in range(student_count):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = [grade]
    else:
        grades[name].append(grade)
else:
    for key, value in sorted({k: grades[k] for k in grades.keys() if sum(grades[k]) / len(grades[k]) >= 4.50}.items(), key=lambda x: -(sum(x[1]) / len(x[1]))):
        print(f'{key} -> {sum(value) / len(value):.2f}')
