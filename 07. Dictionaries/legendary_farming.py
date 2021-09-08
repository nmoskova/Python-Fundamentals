key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
legendary_item = ""

while legendary_item == "":
    materials = input().split()

    for i in range(1, len(materials), 2):
        material = materials[i].lower()
        qty = int(materials[i-1])

        if material == "shards":
            key_materials["shards"] += qty
        elif material == "fragments":
            key_materials["fragments"] += qty
        elif material == "motes":
            key_materials["motes"] += qty
        else:

            if material not in junk:
                junk[material] = qty
            else:
                junk[material] += qty

        if key_materials["shards"] >= 250:
            key_materials["shards"] -= 250
            legendary_item = "Shadowmourne"
            break
        elif key_materials["fragments"] >= 250:
            key_materials["fragments"] -= 250
            legendary_item = "Valanyr"
            break
        elif key_materials["motes"] >= 250:
            key_materials["motes"] -= 250
            legendary_item = "Dragonwrath"
            break

print(f"{legendary_item} obtained!")
sorted_key_materials = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))

for key, value in sorted_key_materials:
    print(f"{key}: {value}")

sorted_junk = sorted(junk.items(), key=lambda x: x[0])
for key, value in sorted_junk:
    print(f"{key}: {value}")



