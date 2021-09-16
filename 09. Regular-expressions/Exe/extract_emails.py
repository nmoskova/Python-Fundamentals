import re

pattern = r"(^|\s)(?P<url>(?P<user>[A-Za-z0-9]+[A-Za-z0-9\.\_\-]*)@(?P<host>[A-Za-z]+([A-Za-z\-]*\.[A-Za-z]+[A-Za-z\-]*)+))"
text = input()

matches = re.finditer(pattern, text)
[print(match.group("url")) for match in matches]