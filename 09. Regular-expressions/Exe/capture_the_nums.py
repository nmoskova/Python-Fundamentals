import re

pattern = r"\d+"

text = input()
while text:
    nums = re.findall(pattern, text)

    if nums:
        print(*nums, end=" ")

    text = input()
