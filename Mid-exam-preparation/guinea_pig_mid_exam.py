food_gr = float(input()) * 1000  # per 1 month -> 30 days
hay_gr = float(input()) * 1000  # per 1 month -> 30 days
cover_gr = float(input()) * 1000  # per 1 month -> 30 days
weight_gr = float(input()) * 1000
enough_food = True

for day in range(1, 31):

    if food_gr > 0 and hay_gr > 0 and cover_gr > 0:
        food_gr -= 300

        if food_gr <= 0:
            enough_food = False
            break

        if day % 2 == 0:
            hay_gr -= 0.05 * food_gr

        if day % 3 == 0:
            cover_gr -= (weight_gr / 3)
    else:
        enough_food = False

if not enough_food:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_gr/1000:.2f}, Hay: {hay_gr/1000:.2f}, "
          f"Cover: {cover_gr/1000:.2f}.")