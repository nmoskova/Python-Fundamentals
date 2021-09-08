command = input()
products = {}

while not command == "buy":
    name, price, qty = command.split()

    if name not in products:
        products[name] = {"price": float(price), "quantity": int(qty)}
        command = input()
        continue

    if not products[name]["price"] == float(price):
        products[name]["price"] = float(price)
    products[name]["quantity"] += int(qty)
    command = input()

for name, values in products.items():
    print(f"{name} -> {(products[name]['price'] * products[name]['quantity']):.2f}")



