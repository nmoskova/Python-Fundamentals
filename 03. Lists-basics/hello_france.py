items_prices_list = input().split('|')
budget_start = float(input())
budget = budget_start
budget_is_enough = False
income_sold_items = 0

for item in items_prices_list:

    price_in_range = False
    splitted_item = item.split('->')
    type_of_item = splitted_item[0]
    price = float(splitted_item[1])

    if type_of_item == 'Clothes' and 0 < price <= 50 and budget >= price:
        price_in_range = True

    elif type_of_item == 'Shoes' and 0 < price <= 35 and budget >= price:
        price_in_range = True

    elif type_of_item == 'Accessories' and 0 < price <= 20.50 and budget >= price:
        price_in_range = True

    if price_in_range:
        budget -= price
        sells_price = price * 1.40
        income_sold_items += sells_price
        print(f'{sells_price:.2f}', end=' ')
print()

budget += income_sold_items
profit = budget - budget_start

print(f'Profit: {profit:.2f}')
if budget >= 150:
    print('Hello, France!')
else:
    print("Time to go.")
