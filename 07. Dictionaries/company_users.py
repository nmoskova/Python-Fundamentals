companies_employees = {}
command = input()

while not command == "End":
    company_name, employee_id = command.split(" -> ")

    if company_name not in companies_employees:
        companies_employees[company_name] = []

    if employee_id not in companies_employees[company_name]:
        companies_employees[company_name].append(employee_id)

    command = input()

for company, employees in sorted(companies_employees.items(), key=lambda x: x[0]):
    print(company)

    for employee in employees:
        print(f"-- {employee}")
