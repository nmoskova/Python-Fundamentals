import re

pattern = r"(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"
text = input()

valid_phones = re.finditer(pattern, text)
matches = [valid.group() for valid in valid_phones]
print(", ".join(matches))