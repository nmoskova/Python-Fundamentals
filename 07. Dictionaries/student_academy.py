pair_rows = int(input())
students_grades = {}

for _ in range(pair_rows):
    student = input()
    grade = float(input())

    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(grade)

for name, grades in students_grades.items():
    students_grades[name] = (sum(grades)/len(grades))

better_results = {name: avg_grade for (name, avg_grade) in students_grades.items() if avg_grade >= 4.50}

for name, grade in sorted(better_results.items(), key=lambda x: -x[1]):
    print(f"{name} -> {grade:.2f}")