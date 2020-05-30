employee_happiness = list(map(int, input().split(' ')))
happiness_factor = int(input())
employee_happiness = list(map(lambda item: item * happiness_factor, employee_happiness))
average_happiness = sum(employee_happiness) / len(employee_happiness)
happy_employees = [employee for employee in employee_happiness if employee >= average_happiness]

if len(happy_employees) >= len(employee_happiness) / 2:
    print(f'Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(employee_happiness)}. Employees are not happy!')
