def odd_even(number):
    even = 0
    odd = 0

    for each in number:
        digit = int(each)

        if digit % 2 == 0:
            even += digit
        else:
            odd += digit

    return print(f"Odd sum = {odd}, Even sum = {even}")


num = input()
odd_even(num)