nums_list = input().split()
int_nums_list = [int(x) for x in nums_list]
middle = len(nums_list) // 2
time_left = 0
time_right = 0

for first in range(0, middle):
    if int_nums_list[first] == 0:
        time_left *= 0.8
    else:
        time_left += int_nums_list[first]

for second in range(-1, -middle-1, -1):
    if int_nums_list[second] == 0:
        time_right *= 0.8
    else:
        time_right += int_nums_list[second]

winner = min(time_left, time_right)

if winner == time_left:
    print(f"The winner is left with total time: {time_left:.1f}")
else:
    print(f"The winner is right with total time: {time_right:.1f}")