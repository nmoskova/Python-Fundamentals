some_string = input()
new_password = some_string

while True:
    command = input()

    if command == "Done":
        break

    data = command.split()
    action = data[0]

    if action == "TakeOdd":
        new_string = ""

        for i in range(1, len(new_password), 2):
            new_string += new_password[i]
        new_password = new_string
        print(new_password)

    elif action == "Cut":
        start_index, length = int(data[1]), int(data[2])
        new_password = new_password[:start_index] + new_password[start_index+length:]
        print(new_password)

    elif action == "Substitute":
        substring, substitute = data[1], data[2]

        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)

        else:
            print("Nothing to replace!")

print(f"Your password is: {new_password}")