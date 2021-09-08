participants = {}
command = input()

while not command == "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)

    if contest not in participants:
        participants[contest] = {username: points}

    else:
        if username in participants[contest]:
            if participants[contest][username] < points:
                participants[contest][username] = points
        else:
            participants[contest].update({username: points})

    command = input()

for c, data in participants.items():
    print(f"{c}: {len(data)} participants")
    position = 1

    for un, p in sorted(data.items(), key=lambda x: (-x[1], x[0])):

        print(f"{position}. {un} <::> {p}")
        position += 1

print(f"Individual standings:")

part_points = {}
for con, data in participants.items():
    for un, p in data.items():
        if un in part_points:
            part_points[un] += p
        else:
            part_points[un] = p

position = 1
for un, p in sorted(part_points.items(), key=lambda x: (-x[1], x[0])):

    print(f"{position}. {un} -> {p}")
    position += 1







