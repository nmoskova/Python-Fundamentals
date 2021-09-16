destinations = input()

while True:
    command = input()

    if command == "Travel":
        break

    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        index = int(command[1])
        given_string = command[2]

        if index in range(len(destinations)):
            destinations = destinations[:index] + given_string + destinations[index:]
        print(destinations)

    elif action == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])

        if (start_index and end_index) in range(len(destinations)):
            destinations = destinations[:start_index] + destinations[(end_index+1):]
        print(destinations)

    elif action == "Switch":
        old_string, new_string = command[1], command[2]

        if old_string in destinations:
            destinations = destinations.replace(old_string, new_string)
        print(destinations)

print(f"Ready for world tour! Planned stops: {destinations}")