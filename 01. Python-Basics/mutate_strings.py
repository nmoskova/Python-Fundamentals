first_string = input()
second_string = input()
unique_string = first_string

for symbol in range(len(second_string)):
    first_part = second_string[:symbol+1]
    second_part = first_string[symbol+1:]
    new_string = first_part + second_part

    if new_string == unique_string:
        continue

    else:
        unique_string = new_string
        print(unique_string)