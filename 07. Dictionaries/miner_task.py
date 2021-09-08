resource = input()
miners_task = {}

while not resource == "stop":
    quantity = int(input())

    if resource not in miners_task:
        miners_task[resource] = 0
    miners_task[resource] += quantity

    resource = input()

for res, qty in miners_task.items():
    print(f"{res} -> {qty}")