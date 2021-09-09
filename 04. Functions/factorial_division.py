def factorial(num):
    factorial_num = 1

    for digit in range(1, num+1):
        factorial_num *= digit

    return factorial_num


def division_factorials(num1, num2):
    division = factorial(num1) / factorial(num2)

    return division


num1 = int(input())
num2 = int(input())

print(f'{(division_factorials(num1, num2)):.2f}')