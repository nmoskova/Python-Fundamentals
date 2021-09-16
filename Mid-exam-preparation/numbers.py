numbers = [int(x) for x in input().split()]
average = sum(numbers) / len(numbers)
above_average = sorted([x for x in numbers if x > average], reverse=True)

if len(above_average) == 0:
    print("No")
else:
    print(*above_average[:5])