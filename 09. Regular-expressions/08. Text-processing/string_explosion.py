some_string = input()
i = 0
bomb_strength = 0
new_string = ""

while i < len(some_string):

    if not some_string[i] == ">" and bomb_strength == 0:
        new_string += some_string[i]

    elif some_string[i] == ">":
        bomb_strength += int(some_string[i+1])
        new_string += ">"
        bomb_strength -= 1
        i += 2
        continue

    if bomb_strength > 0:
        bomb_strength -= 1

    i += 1

print(new_string)