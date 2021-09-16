import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

text = input()
print(*(re.findall(pattern, text)))