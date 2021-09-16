concealed_message = input()
data = input()

while not data == "Reveal":
    data = data.split(":|:")
    command = data[0]

    if command == "InsertSpace":
        index = int(data[1])
        first_part = concealed_message[:index] + " "
        second_part = concealed_message[index:]
        concealed_message = first_part + second_part
        print(concealed_message)

    elif command == "Reverse":
        substring = data[1]

        if substring not in concealed_message:
            print("error")
        else:
            concealed_message = concealed_message.replace(substring, "", 1)
            substring = substring[::-1]
            concealed_message += substring
            print(concealed_message)

    elif command == "ChangeAll":
        substring = data[1]
        replacement = data[2]

        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
            print(concealed_message)

    data = input()

print(f"You have a new text message: {concealed_message}")
