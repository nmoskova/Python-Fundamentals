import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()

valid_nums = re.finditer(pattern, text)
valid_nums = [n.group() for n in valid_nums]
print(*valid_nums)