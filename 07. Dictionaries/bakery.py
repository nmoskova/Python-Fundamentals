food_list = input().split()
bakery = {}

for index in range(0, len(food_list)-1, 2):
    bakery[food_list[index]] = int(food_list[index + 1])

print(bakery)
