some_string = input()
i = 0
new_string = ""

while i < len(some_string):

    if i == 0:
        new_string += some_string[i]

    else:

        if some_string[i] != new_string[-1]:
            new_string += some_string[i]

    i += 1

print(new_string)