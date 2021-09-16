count_students = int(input())
count_lectures = int(input())
initial_bonus = int(input())
max_bonus = 0
attendances_max = 0

for student in range(count_students):

    attendance = int(input())
    total_bonus = attendance / count_lectures * (5 + initial_bonus)

    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        attendances_max = attendance

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {attendances_max} lectures.")
