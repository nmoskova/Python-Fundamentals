people_waiting = int(input())
wagons = [int(x) for x in input().split() if 0 <= int(x) <= 4]

for index in range(len(wagons)):
    if people_waiting > 0:

        if wagons[index] < 4:
            people_waiting -= (4 - wagons[index])
            wagons[index] += (4 - wagons[index])

            if people_waiting < 0:
                wagons[-1] += people_waiting
                people_waiting = 0

if people_waiting == 0 and sum(wagons) < len(wagons) * 4:
    print("The lift has empty spots!")
elif people_waiting > 0 and sum(wagons) == len(wagons) * 4:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

print(*wagons, sep=' ')