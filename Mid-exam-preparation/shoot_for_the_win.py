targets = [int(x) for x in input().split()]
command = input()
shot_targets = 0

while not command == "End":
    index = int(command)

    if index in range(len(targets)):
        if not targets[index] == -1:
            for i in range(len(targets)):
                if not i == index:

                    if targets[i] <= targets[index] and not targets[i] == -1:
                        targets[i] += targets[index]
                    elif targets[i] > targets[index]:
                        targets[i] -= targets[index]

            targets[index] = -1
            shot_targets += 1

    command = input()

print(f"Shot targets: {shot_targets} -> {' '.join([str(x) for x in targets])}")