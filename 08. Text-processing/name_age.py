import re

pattern_name = r"@(?P<name>[A-Za-z]+)\|"
pattern_age = r"#(?P<age>\d+)\*"

n = int(input())

for _ in range(n):
    text = input()
    name = ""
    age = 0

    for match in re.finditer(pattern_name, text):
        name = match.group("name")

    for match in re.finditer(pattern_age, text):
        age = match.group("age")
    print(f"{name} is {age} years old.")
