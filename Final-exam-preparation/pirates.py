aimed_cities = {}
command = input()

while not command == "Sail":
    command = command.split("||")
    city = command[0]
    population = int(command[1])
    gold = int(command[2])

    if city not in aimed_cities:
        aimed_cities[city] = {"population": population, "gold": gold}
    else:
        aimed_cities[city]["population"] += population
        aimed_cities[city]["gold"] += gold

    command = input()

command = input()
while not command == "End":
    command = command.split("=>")
    action = command[0]

    if action == "Plunder":
        city_attacked = command[1]
        people_killed = int(command[2])
        gold_stealed = int(command[3])

        if city_attacked in aimed_cities:
            aimed_cities[city_attacked]["population"] -= people_killed
            aimed_cities[city_attacked]["gold"] -= gold_stealed
            print(f"{city_attacked} plundered! {gold_stealed} gold stolen, {people_killed} citizens killed.")

            if aimed_cities[city_attacked]["population"] <= 0 or aimed_cities[city_attacked]["gold"] <= 0:
                print(f"{city_attacked} has been wiped off the map!")
                aimed_cities.pop(city_attacked)

    elif action == "Prosper":
        prospered_town = command[1]
        increased_amount_gold = int(command[2])

        if prospered_town in aimed_cities:

            if increased_amount_gold < 0:
                print("Gold added cannot be a negative number!")
            else:
                aimed_cities[prospered_town]["gold"] += increased_amount_gold
                print(f"{increased_amount_gold} gold added to the city treasury. {prospered_town}"
                      f" now has {aimed_cities[prospered_town]['gold']} gold.")
    command = input()

if len(aimed_cities) > 0:
    print(f"Ahoy, Captain! There are {len(aimed_cities)} wealthy settlements to go to:")
    sorted_cities = dict(sorted(aimed_cities.items(), key=lambda x: (-x[1]["gold"], x[0])))

    for city, data in sorted_cities.items():
        print(f"{city} -> Population: {sorted_cities[city]['population']} citizens,"
              f" Gold: {sorted_cities[city]['gold']} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

