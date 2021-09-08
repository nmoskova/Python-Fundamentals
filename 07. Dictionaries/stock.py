products = input().split(" ")
searched_products = input().split(" ")
stock = {}

for index in range(0, len(products), 2):
    stock[products[index]] = int(products[index+1])

for s_p in searched_products:
    if s_p in stock:
        print(f"We have {stock[s_p]} of {s_p} left")
    else:
        print(f"Sorry, we don't have {s_p}")
