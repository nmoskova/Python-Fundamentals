some_string = input()

while True:
    command = input()

    if command == "End":
        break

    command = command.split()
    action = command[0]

    if action == "Translate":
        char = command[1]
        replacement = command[2]

        if char in some_string:
            some_string = some_string.replace(char, replacement)
            print(some_string)

    elif action == "Includes":
        string = command[1]

        if string in some_string:
            print("True")
        else:
            print("False")

    elif action == "Start":
        string = command[1]
        string_to_check = some_string[:len(string)]

        if string_to_check == string:
            print("True")
        else:
            print("False")

    elif action == "Lowercase":
        some_string = some_string.lower()
        print(some_string)

    elif action == "FindIndex":
        char = command[1]
        last_index = -1

        for i in range(len(some_string)):
            if some_string[i] == char:
                last_index = i
        print(last_index)

    elif action == "Remove":
        start_index = int(command[1])
        end_index = start_index + int(command[2])
        some_string = some_string[:start_index] + some_string[(end_index):]
        print(some_string)