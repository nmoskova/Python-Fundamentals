import re

pattern = r"\b_(?P<wanted_string>[A-Za-z0-9]+)\b"
text = input()
matches = []

wanted = re.finditer(pattern, text)
for w in wanted:
    matches.append(w.group("wanted_string"))

print(f"{','.join(matches)}")
