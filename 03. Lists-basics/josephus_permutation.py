nums_list = input().split()
k = int(input())
new_string = []
counter = 0
index = 0

while nums_list:
    counter += 1
    if counter % k == 0:
        new_string.append(nums_list.pop(index))
    else:
        index += 1
    if index >= len(nums_list):
        index = 0

print('[', end='')

for each in range(len(new_string)):

    if each == (len(new_string)-1):
        print(f'{new_string[each]}]')

    else:
        print(f'{new_string[each]},', end='')
