def sum_numbers(n1: int, n2: int):
    return n1 + n2


def subtract(sum_int: int, n3: int):
    return sum_int - n3


def add_and_subtract(num_1: int, num_2: int, num_3: int):
    sum_num = sum_numbers(num_1, num_2)
    subtr = subtract(sum_num, num_3)
    return subtr


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))