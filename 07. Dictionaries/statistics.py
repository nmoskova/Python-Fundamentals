command = input()
in_stock = {}

while not command == "statistics":
    pr_name, pr_quantity = command.split(":")

    if pr_name not in in_stock:
        in_stock[pr_name] = int(pr_quantity)

    else:
        in_stock[pr_name] += int(pr_quantity)
    command = input()

print("Products in stock:")

for k in in_stock:
    print(f"- {k}: {in_stock[k]}")

print(f"Total Products: {len(in_stock)}")
print(f"Total Quantity: {sum(in_stock.values())}")


