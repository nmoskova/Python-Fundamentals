array = [int(x) for x in input().split()]
command = input()

while not command == "end":

    if not command == "decrease":
        action, num1, num2 = command

        if action == "swap":
            array[num1], array[num2] = array[num2], array[num1]
        elif action == "multiply":
            array[num1] = array[num1] * array[num2]
    else:
        array = [x-1 for x in array]

    command = input()

print(*array, sep=", ")