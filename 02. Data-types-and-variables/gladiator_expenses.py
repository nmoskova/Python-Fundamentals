lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
count_shield_breakage = 0

for loss in range(1, lost_fights_count + 1):

    if loss % 2 == 0:
        total_expenses += helmet_price

    if loss % 3 == 0:
        total_expenses += sword_price

    if loss % 2 == 0 and loss % 3 == 0:  # shield is broken
        count_shield_breakage += 1
        total_expenses += shield_price
        if count_shield_breakage % 2 == 0:
            total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")