first_string = input().split(", ")
second_string = input().split(", ")
new_string = []

for el in first_string:
    for sec_el in second_string:

        if el in sec_el:
            new_string.append(el)
            break

print(new_string)