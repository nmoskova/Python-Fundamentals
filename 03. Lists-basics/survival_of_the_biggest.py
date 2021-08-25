numbers = input().split()
to_remove = int(input())

# for i in range(0, len(numbers)):
#     numbers[i] = int(numbers[i])
numbers = [int(x) for x in numbers]

for _ in range(to_remove):
    numbers.remove(min(numbers))

for i in range(0, len(numbers)):
    numbers[i] = str(numbers[i])

print(', '.join(numbers))




