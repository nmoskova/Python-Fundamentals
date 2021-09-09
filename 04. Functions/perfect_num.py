def perfect_num(num):
    sum_divisors = 0

    for digit in range(1, num):

        if num % digit == 0:
            sum_divisors += digit

    if num == sum_divisors:
        return True
    else:
        return False


num = int(input())

if perfect_num(num):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")

