command = input()
chat = []

while not command == "end":
    command = command.split()
    action = command[0]

    if action == "Chat":
        message = command[1]
        chat.append(message)

    elif action == "Delete":
        message = command[1]
        if message in chat:
            chat.remove(message)  # няма да работи ако съобщението се повтаря, da se napravi s for loop

    elif action == "Edit":
        message_to_edit = command[1]
        edited_message = command[2]
        if message_to_edit in chat:
            index = chat.index(message_to_edit)
            chat[index] = edited_message

    elif action == "Pin":
        message = command[1]
        if message in chat:
            chat.append(message)
            chat.remove(message)

    elif action == "Spam":
        chat += command[1:]

    command = input()

[print(x) for x in chat]