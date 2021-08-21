num = int(input())
stars = 0

for nums in range(1, num + 1):
    print('*' * nums)

for nums in range(num - 1, 0, -1):
    print('*' * nums)