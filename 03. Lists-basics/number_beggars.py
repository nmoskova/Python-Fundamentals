n = input().split(', ')
beggars = int(input())
sum_collected = []
count = 0

while count < beggars:
    sum_beggar = 0

    for each_num in range(count, len(n), beggars):
        sum_beggar += int(n[each_num])

    sum_collected.append(sum_beggar)
    count += 1

print(sum_collected)

