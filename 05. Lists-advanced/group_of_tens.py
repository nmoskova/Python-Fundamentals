numbers = [int(x) for x in input().split(", ")]
group = 10

while numbers:
    group_list = []
    [group_list.append(each) for each in numbers if each <= group]
    [numbers.remove(number) for number in group_list if number in numbers]
    print(f"Group of {group}'s: {group_list}")
    group += 10
