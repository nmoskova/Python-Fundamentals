import re

pattern = r"\b\d{2}\b"
text = input()

print(re.findall(pattern, text))

