exams = {}
students = {}

while True:
    input_string = input()
    if input_string == 'exam finished':

        print('Results:')
        sorted_results = list(sorted([item for current_list in students.values() for item in current_list], key=lambda x: (-x[1], x[0])))
        for item in sorted_results:
            for key, value in students.items():
                if item in value:
                    print(f'{key} | {item[1]}')
                    value.remove(item)
                    continue

        print('Submissions:')
        for key, value in sorted(exams.items(), key=lambda x: (-x[1], x[0])):
            print(f'{key} - {value}')

        break
    else:
        if 'banned' in input_string:
            args = input_string.split('-')
            username = args[0]
            if username in students:
                del students[username]
        else:
            args = input_string.split('-')
            username = args[0]
            language = args[1]
            points = int(args[2])

            if username not in students:
                students[username] = [[language, points]]
            else:
                attended_exams = [item[0] for item in students[username]]
                if language in attended_exams:
                    for item in students[username]:
                        if item[0] == language and item[1] <= points:
                            item[1] = points
                else:
                    students[username].append([language, points])

            if language in exams:
                exams[language] += 1
            else:
                exams[language] = 1


