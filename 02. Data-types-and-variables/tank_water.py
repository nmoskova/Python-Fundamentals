times_pour_water = int(input())
capacity = 255
filled = 0

for each_pour in range(times_pour_water):
    liters_to_pour = int(input())

    if capacity >= liters_to_pour:
        capacity -= liters_to_pour
        filled += liters_to_pour

    else:
        print("Insufficient capacity!")

print(filled)