quantity_allowed = int(input())
days_left = int(input())

christmas_spirit = 0
total_cost = 0
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for day in range(1, days_left+1):
    if day % 11 == 0:
        quantity_allowed += 2
    if day % 2 == 0:
        christmas_spirit += 5
        total_cost += ornament_set * quantity_allowed
    if day % 3 == 0:
        christmas_spirit += 13
        total_cost += (tree_skirt + tree_garlands) * quantity_allowed
    if day % 5 == 0:
        christmas_spirit += 17
        total_cost += tree_lights * quantity_allowed
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        total_cost += tree_skirt + tree_garlands + tree_lights

if days_left % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {total_cost} \nTotal spirit: {christmas_spirit}')
