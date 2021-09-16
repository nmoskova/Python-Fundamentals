activation_key = input()
command = input()

while not command == "Generate":
    data = command.split(">>>")

    if "Contains" in data:
        substring = data[1]

        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif "Flip" in data:
        action = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        modified_string = ""

        if action == "Upper":
            modified_string = activation_key[start_index:end_index].upper()

        elif action == "Lower":
            modified_string = activation_key[start_index:end_index].lower()
        activation_key = activation_key.replace(activation_key[start_index:end_index], modified_string)
        print(activation_key)

    elif "Slice" in data:
        start_index = int(data[1])
        end_index = int(data[2])
        activation_key = activation_key.replace(activation_key[start_index:end_index], "")
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
