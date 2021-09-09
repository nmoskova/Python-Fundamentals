import re

pattern_type = r"&(?P<type>[a-zA-Z]+)&"
pattern_coordinates = r"<(?P<coordinates>[A-Za-z0-9]+)>"

keys = [int(key) for key in input().split()]

while True:
    text = input()
    new_text = ""

    if text == "find":
        break

    i = 0
    while i < len(text):
        for key in keys:
            char = text[i]
            new_char = chr(ord(char) - key)
            new_text += new_char
            i += 1
            if i == len(text):
                break

    type_treasure = [match.group("type") for match in re.finditer(pattern_type, new_text)]
    coordinates = [match.group("coordinates") for match in re.finditer(pattern_coordinates, new_text)]
    print(f"Found {''.join(type_treasure)} at {''.join(coordinates)}")


