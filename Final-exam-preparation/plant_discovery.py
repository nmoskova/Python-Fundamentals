n = int(input())
plants = {}

for _ in range(n):
    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])
    plants[plant] = {"rarity": rarity, "rating": []}

while True:
    command = input()

    if command == "Exhibition":
        break

    action = (command.split(": ")[0])

    if action == "Rate":
        info = "".join(command.split(": ")[1])
        plant, rating = info.split(" - ")
        rating = int(rating)

        if plant in plants.keys():
            plants[plant]['rating'].append(rating)
        else:
            print("error")

    elif action == "Update":
        info = "".join(command.split(": ")[1])
        plant, new_rarity = info.split(" - ")
        new_rarity = int(new_rarity)

        if plant in plants.keys():
            plants[plant]["rarity"] = new_rarity
        else:
            print("error")

    elif action == "Reset":
        plant = (command.split(": ")[1])

        if plant in plants.keys():
            plants[plant]["rating"] = []
        else:
            print("error")

for key, value in plants.items():

    if len(value["rating"]) > 0:
        value["rating"] = sum(value["rating"]) / len(value["rating"])
    else:
        value["rating"] = 0

sorted_plants = sorted(plants.items(), key=lambda x: (-x[1]["rarity"], -x[1]["rating"]))

print("Plants for the exhibition:")
for plant, data in sorted_plants:
    print(f"- {plant}; Rarity: {data['rarity']}; Rating: {data['rating']:.2f}")