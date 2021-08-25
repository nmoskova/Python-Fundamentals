string_nums = input()
nums_list = string_nums.split(' ')
new_list = []

for num in nums_list:
    flip_num = -(int(num))
    new_list.append(flip_num)

print(new_list)
