employees = [int(x) for x in input().split()]
factor_happinnes = int(input())
employee_happinnes = [x * factor_happinnes for x in employees]
average_happinnes = sum(employee_happinnes) / len(employee_happinnes)

happy_people = [el for el in employee_happinnes if el >= average_happinnes]
sad_people = [el for el in employee_happinnes if el < average_happinnes]

if len(happy_people) > len(sad_people):
    print(f"Score: {len(happy_people)}/{len(employee_happinnes)}. Employees are happy!")
else:
    print(f"Score: {len(happy_people)}/{len(employee_happinnes)}. Employees are not happy!")