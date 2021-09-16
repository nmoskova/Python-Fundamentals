num_heroes = int(input())
heroes = {}

for _ in range(num_heroes):
    hero_name, hit_points, mana_points = input().split()
    hit_points, mana_points = int(hit_points), int(mana_points)  # max points: HP:100, MP: 200
    heroes[hero_name] = {"hit_points": hit_points, "mana_points": mana_points}

while True:
    data = input()

    if data == "End":
        break

    data = data.split(" - ")
    command = data[0]

    if command == "CastSpell":
        hero_name = data[1]
        mp_needed = int(data[2])
        cast_spell = data[3]

        if heroes[hero_name]["mana_points"] >= mp_needed:
            heroes[hero_name]["mana_points"] -= mp_needed
            print(f"{hero_name} has successfully cast {cast_spell} and now has {heroes[hero_name]['mana_points']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {cast_spell}!")

    elif command == "TakeDamage":
        hero_name, attacker = data[1], data[3]
        damage = int(data[2])
        heroes[hero_name]["hit_points"] -= damage

        if heroes[hero_name]["hit_points"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hit_points']} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command == "Recharge":
        hero_name = data[1]
        mp_recharge_amount = int(data[2])

        if heroes[hero_name]["mana_points"] + mp_recharge_amount >= 200:
            mp_recharge_amount = 200 - heroes[hero_name]["mana_points"]
            heroes[hero_name]["mana_points"] = 200
        else:
            heroes[hero_name]["mana_points"] += mp_recharge_amount
        print(f"{hero_name} recharged for {mp_recharge_amount} MP!")

    elif command == "Heal":
        hero_name = data[1]
        hp_recharged = int(data[2])

        if heroes[hero_name]["hit_points"] + hp_recharged >= 100:
            hp_recharged = 100 - heroes[hero_name]["hit_points"]
            heroes[hero_name]["hit_points"] = 100
        else:
            heroes[hero_name]["hit_points"] += hp_recharged
        print(f"{hero_name} healed for {hp_recharged} HP!")

for name, data in sorted(heroes.items(), key=lambda x: (-x[1]['hit_points'], x[0])):
    # print(name)
    # print(f"  HP: {data['hit_points']}")
    # print(f"  MP: {data['mana_points']}")
    print(f"{name}\n  HP: {data['hit_points']}\n  MP: {data['mana_points']}")