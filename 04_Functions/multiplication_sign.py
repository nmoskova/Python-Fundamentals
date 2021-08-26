def define_the_num(numbers):
    count_negatives = 0

    for each in numbers:
        each = int(each)

        if each == 0:
            return 'zero'
        if each < 0:
            count_negatives += 1

    if count_negatives % 2 == 1:
        return 'negative'
    else:
        return 'positive'


num1 = input()
num2 = input()
num3 = input()

numbers = []

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)

print(define_the_num(numbers))