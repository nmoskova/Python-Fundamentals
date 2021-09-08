dwarfs_data = {}
data = input()

while not data == "Once upon a time":
    name, hat_colour, physics = data.split(" <:> ")
    physics = int(physics)

    if hat_colour not in dwarfs_data:
        dwarfs_data[hat_colour] = {name: physics}

    else:
        if name in dwarfs_data[hat_colour]:
            if dwarfs_data[hat_colour][name] < physics:
                dwarfs_data[hat_colour][name] = physics
        else:
            dwarfs_data[hat_colour].update({name: physics})

    data = input()

extract_info = [(key, el, dwarfs_data[key][el], len(value)) for key, value in dwarfs_data.items() for el in value]
order = sorted(extract_info, key=lambda x: (int(x[2]), x[3]), reverse=True)
for i in order:
    print(f"({i[0]}) {i[1]} <-> {i[2]}")




