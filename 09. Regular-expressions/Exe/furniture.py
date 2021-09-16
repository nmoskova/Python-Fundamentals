import re

total_cost = 0
bought_furniture = []
pattern = r">>(?P<furniture_name>[A-Z]+[A-Za-z]+)<<(?P<price>\d+.?\d+)!(?P<qty>\d+)"

purchase = input()
while not purchase == "Purchase":
    matches = re.match(pattern, purchase)

    if matches:
        furniture_name = matches.group("furniture_name")
        bought_furniture.append(furniture_name)
        total_cost += (float(matches.group("price")) * int(matches.group("qty")))

    purchase = input()

print("Bought furniture:")
[print(bf) for bf in bought_furniture]
print(f"Total money spend: {total_cost:.2f}")
