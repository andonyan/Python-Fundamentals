persons = int(input())
capacity = int(input())
courses = 0

if persons % capacity == 0:
    courses = persons // capacity
else:
    courses = persons // capacity + 1

print(courses)