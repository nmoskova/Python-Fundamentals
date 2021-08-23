#  prime num - number greater than 1 that is not a product of two smaller natural numbers

number = int(input())
prime_number = False
count_dividers = 0

for divider in range(1, number + 1):
    if number % divider == 0:
        count_dividers += 1

if count_dividers == 2:
    prime_number = True

print(f'{prime_number}')