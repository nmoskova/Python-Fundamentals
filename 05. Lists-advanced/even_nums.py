numbers = input().split(", ")

even = [index for index in range(len(numbers)) if int(numbers[index]) % 2 == 0]
print(even)