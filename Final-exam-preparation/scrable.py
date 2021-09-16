string = input()
new_word = string

while True:
    command = input()
    data = command.split()
    action = data[0]

    if action == "Move":
        index = int(data[1])

        if index in range(len(new_word)):
            to_add_at_the_end = new_word[index]
            new_word = new_word.replace(to_add_at_the_end, "", 1)
            new_word += to_add_at_the_end

    elif action == "Insert" and data[1] == "Space":
        index = int(data[2])
        new_word = new_word[:index] + ' ' + new_word[index:]

    elif action == "Reverse":
        substring = data[1]

        if substring in new_word:
            new_word = new_word.replace(substring, "", 1) + substring[::-1]

    elif action == "Exchange" and data[1] == "Tiles":
        new_letters = data[2]
        new_word = new_letters + new_word[len(new_letters):]
        print(*new_word, sep=" ")
        break

    elif command == "Pass":
        print(*new_word, sep=" ")
        break

    elif command == "Play":
        print(f"You are playing with the word {(new_word.split()[0])}")
        break