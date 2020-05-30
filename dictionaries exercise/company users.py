companies = {}

while True:
    tokens = input().split(' -> ')
    if tokens[0] == 'End':
        for key, value in sorted(companies.items(), key=lambda x: x[0]):
            print(f'{key}')
            for emp in value:
                print(f'-- {emp}')
        break
    else:
        company = tokens[0]
        employee = tokens[1]
        if company not in companies:
            companies[company] = [employee]
        else:
            if employee not in companies[company]:
                companies[company].append(employee)
