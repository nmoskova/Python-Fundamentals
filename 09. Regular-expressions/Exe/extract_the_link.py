import re

pattern = r"(?P<link>www\.[A-Za-z]+[A-Za-z\d\-]*(\.[a-z]+)+)"
text = input()

while text:
    matches = re.finditer(pattern, text)

    for match in matches:
        print(match.group("link"))

    text = input()

