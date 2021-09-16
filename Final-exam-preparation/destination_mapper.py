import re

pattern = r"(?P<delimiter>=|\/)(?P<word>[A-Z][A-Za-z]{2,})(?P=delimiter)"
text = input()
destinations = []

for match in re.finditer(pattern, text):
    destinations.append(match.group("word"))

print(f'Destinations: {", ".join(destinations)}')

count = 0
for destination in destinations:
    count += len(destination)

print(f"Travel Points: {count}")