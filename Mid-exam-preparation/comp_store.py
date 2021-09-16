command = input()
total = 0

while not command == "special" and not command == "regular":
    price = float(command)

    if price < 0:
        print("Invalid price!")
    elif price == 0:
        print("Invalid order!")
    else:
        total += price

    command = input()

taxes = total * 0.20
total_plus_taxes = total + taxes

if command == "special":
    total_plus_taxes *= 0.9

if total == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n\
Price without taxes: {total:.2f}$\n\
Taxes: {taxes:.2f}$\n\
-----------\n\
Total price: {total_plus_taxes:.2f}$")