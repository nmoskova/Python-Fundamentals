letters = "0abcdefghijklmnopqrstuvwxyz"
total = 0
num_betw_two_letters = input().split()
number = ""

for each in num_betw_two_letters:
    first_letter = each[0]
    last_letter = each[-1]
    position_first_letter = letters.index(first_letter.lower())
    position_last_letter = letters.index(last_letter.lower())

    for ch in each:
        if ch.isdigit():
            number += ch
    number = int(number)

    if first_letter.isupper():
        total += number / position_first_letter
    elif first_letter.islower():
        total += position_first_letter * number

    if last_letter.isupper():
        total -= position_last_letter
    elif last_letter.islower():
        total += position_last_letter
    number = ""

print(f"{total:.2f}")