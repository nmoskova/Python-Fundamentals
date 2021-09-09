def calculation(operator, num1, num2):

    if operator == 'multiply':
        return num1 * num2

    elif operator == 'divide':
        return int(num1 / num2)

    elif operator == 'sum':
        return num1 + num2

    elif operator == 'subtract':
        return num1 - num2

    else:
        return None


operator = input()
number1 = int(input())
number2 = int(input())
print(calculation(operator, number1, number2))