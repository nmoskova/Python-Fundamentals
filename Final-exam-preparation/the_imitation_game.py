message = input()

while True:
    command = input()

    if command == "Decode":
        break

    command = command.split("|")
    action = command[0]

    if action == "Move":
        num_letters = int(command[1])
        message = message[num_letters:] + message[:num_letters]

    elif action == "Insert":
        index, value = command[1], command[2]
        index = int(index)
        message = message[:index] + value + message[index:]

    elif action == "ChangeAll":
        substr, replacement = command[1], command[2]
        message = message.replace(substr, replacement)

print(f"The decrypted message is: {message}")