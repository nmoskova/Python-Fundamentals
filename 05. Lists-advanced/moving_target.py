def is_index_valid(seq_of_targets: list, index: int):
    if index in range(len(seq_of_targets)):
        return True
    else:
        return False


def shoot(seq_of_targets: list, index: int, value: int):
    if is_index_valid(seq_of_targets, index):
        seq_of_targets[index] -= value
        if seq_of_targets[index] <= 0:
            seq_of_targets.pop(index)


def add(seq_of_targets: list, index: int, value: int):
    if is_index_valid(seq_of_targets, index):
        seq_of_targets.insert(index, value)
    else:
        return print("Invalid placement!")


def strike(seq_of_targets: list, index: int, value: int):
    if is_index_valid(seq_of_targets, index+value) and is_index_valid(seq_of_targets, index-value):
        for ind in range((index + value), (index - value-1), -1):
            seq_of_targets.pop(ind)
    else:
        return print("Strike missed!")


seq_of_targets = [int(x) for x in input().split(" ")]

command = input()

while not command == "End":
    action, index, value = command.split(" ")
    index = int(index)
    value = int(value)

    if action == "Shoot":
        shoot(seq_of_targets, index, value)

    elif action == "Add":
        add(seq_of_targets, index, value)

    elif action == "Strike":
        strike(seq_of_targets, index, value)

    command = input()


print(* seq_of_targets, sep="|")




