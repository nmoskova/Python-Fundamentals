data = input()
courses = {}

while ":" in data:
    name, id, course = data.split(":")

    if course not in courses:
        courses[course] = {}
    courses[course][id] = name

    data = input()

searched_course = " ".join(data.split("_"))

if searched_course in courses:
    for id, name in courses[searched_course].items():
        print(f"{name} - {id}")
