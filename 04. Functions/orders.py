def order(prod, quantity):

    if prod == 'coffee':
        return 1.50 * quantity

    elif prod == 'water':
        return 1.00 * quantity

    elif prod == 'coke':
        return 1.40 * quantity

    elif prod == 'snacks':
        return 2.00 * quantity


product = input()
quantity = int(input())

print(f'{order(product, quantity):.2f}')