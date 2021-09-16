def index_is_valid(weapon: list, index: int):
    if index in range(len(weapon)):
        return True
    return False


weapon = input().split("|")
data = input()

while not data == "Done":
    command = data.split()

    if command[0] == "Add":
        particle = command[1]
        index = int(command[2])

        if index_is_valid(weapon, index):
            weapon.insert(index, particle)

    elif command[0] == "Remove":
        index = int(command[1])

        if index_is_valid(weapon, index):
            weapon.pop(index)

    elif command[1] == "Even":
        even = [weapon[i] for i in range(len(weapon)) if i % 2 == 0]
        print(" ".join(even))

    elif command[1] == "Odd":
        odd = [weapon[i] for i in range(len(weapon)) if not i % 2 == 0]
        print(" ".join(odd))

    data = input()

print(f"You crafted {''.join(weapon)}!")