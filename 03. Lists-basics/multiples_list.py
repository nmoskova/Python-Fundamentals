factor = int(input())
count = int(input())
nums_list = []
dividend = 1

while len(nums_list) < count:

    if dividend % factor == 0:
        nums_list.append(dividend)
    dividend += 1

print(nums_list)
