budget = float(input())
price_per_kg_flour = float(input())

price_per_pack_eggs = 0.75 * price_per_kg_flour
price_per_milk = 1.25 * price_per_kg_flour
cozonacs_made = 0
colored_eggs_gathered = 0
cost_per_cozunak = price_per_pack_eggs + price_per_kg_flour + price_per_milk/4

while budget >= cost_per_cozunak:
    budget -= cost_per_cozunak
    cozonacs_made += 1
    colored_eggs_gathered += 3

    if cozonacs_made % 3 == 0:
        colored_eggs_gathered -= (cozonacs_made - 2)

print(f'You made {cozonacs_made} cozonacs! Now you have {colored_eggs_gathered} eggs and {budget:.2f}BGN left.')


