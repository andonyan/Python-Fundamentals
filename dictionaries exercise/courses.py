courses = {}

while True:
    tokens = input().split(' : ')
    if tokens[0] == 'end':
        for k, v in sorted(courses.items(), key=lambda x: len(x[1]), reverse=True):
            print(f'{k}: {len(courses[k])}')
            for name in sorted(v):
                print(f'-- {name}')
        break
    else:
        course = tokens[0]
        student = tokens[1]
        if course not in courses:
            courses[course] = [student]
        else:
            courses[course].append(student)
