energy = int(input())
distance = input()
battles_won = 0
enough_energy = True

while not distance == "End of battle":

    if int(distance) > energy:
        enough_energy = False
        break

    else:
        battles_won += 1
        energy -= int(distance)

        if battles_won % 3 == 0:
            energy += battles_won
    distance = input()

if enough_energy:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
