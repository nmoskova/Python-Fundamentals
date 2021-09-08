dragons = {}
n = int(input())

for _ in range(n):
    colour, name, damage, health, armor = input().split()

    if damage == "null":
        damage = 45

    if health == "null":
        health = 250

    if armor == "null":
        armor = 10

    if colour not in dragons:
        dragons[colour] = {name: {"damage": int(damage), "health": int(health), "armor": int(armor)}}
    else:
        dragons[colour].update({name: {"damage": int(damage), "health": int(health), "armor": int(armor)}})

for col_dragon, data in dragons.items():
    avg_damage = 0
    avg_health = 0
    avg_armor = 0
    drag_col_print = []

    for name, kvp in sorted(data.items(), key=lambda x: x[0]):
        avg_damage += kvp["damage"]
        avg_health += kvp["health"]
        avg_armor += kvp["armor"]
        dragon = f'-{name} -> damage: {kvp["damage"]}, health: {kvp["health"]}, armor: {kvp["armor"]}'
        drag_col_print.append(dragon)

    avg_damage = avg_damage / len(data)
    avg_health = avg_health / len(data)
    avg_armor = avg_armor / len(data)

    print(f"{col_dragon}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    print("\n".join(drag_col_print))