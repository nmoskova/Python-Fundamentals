n = int(input())
# for num in range(1, n + 1):
#     num_as_string = str(num)
#     sum_symbols = 0
#     for symbol in num_as_string:
#         sum_symbols += int(symbol)
#     special_num = (sum_symbols == 5) or (sum_symbols == 7) or (sum_symbols == 11)
#     print(f'{num} -> {special_num}')

for num in range(1, n+1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
       sum_of_digits += digits % 10
       digits = digits // 10
    special_num = (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11)
    print(f'{num} -> {special_num}')