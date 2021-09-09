some_text = input()
message_to_multiply = ""
new_message = ""
number = ""
i = 0

while i < len(some_text):

    if not some_text[i].isdigit():
        message_to_multiply += some_text[i]
    else:
        number += some_text[i]

        while i < len(some_text):

            if (i+1) < len(some_text) and some_text[i+1].isdigit():
                number += some_text[i+1]
                i += 1
            else:
                new_message += message_to_multiply * int(number)
                message_to_multiply = ""
                number = ""
                break

    i += 1

print(f"Unique symbols used: {len(set(new_message.upper()))}")
print(new_message.upper())
