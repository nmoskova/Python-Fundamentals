list_fire = input().split('#')
water_quantity = int(input())
effort = 0
total_fire = 0
water_cells_list = []

for each_type in list_fire:
    enough_water = False
    each_type_list = each_type.split(' ')
    type_of_fire = each_type_list[0]
    water_cell = int(each_type_list[2])

    if type_of_fire == 'High' and water_cell in range(81, 126) and water_cell <= water_quantity:
        enough_water = True

    elif type_of_fire == 'Medium' and water_cell in range(51, 81) and water_cell <= water_quantity:
        enough_water = True

    elif type_of_fire == 'Low' and water_cell in range(1, 51) and water_cell <= water_quantity:
        enough_water = True

    if enough_water:
        water_quantity -= water_cell
        effort += 0.25 * water_cell
        total_fire += water_cell
        water_cells_list.append(water_cell)

print('Cells:')
for each_cell in water_cells_list:
    print(f' - {each_cell}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')