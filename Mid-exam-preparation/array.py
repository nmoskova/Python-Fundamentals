array = [int(x) for x in input().split()]
command = input()

while not command == "end":

    if not command == "decrease":
        action, num1, num2 = command.split()

        if action == "swap":
            array[int(num1)], array[int(num2)] = array[int(num2)], array[int(num1)]
        elif action == "multiply":
            array[int(num1)] = array[int(num1)] * array[int(num2)]

    else:
        array = [x-1 for x in array]

    command = input()

print(*array, sep=", ")