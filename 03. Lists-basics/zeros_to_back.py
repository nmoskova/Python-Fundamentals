numbers_list = input().split(', ')

for number in numbers_list:

    if number == '0':
        numbers_list.append(number)
        numbers_list.remove(number)

str_to_int = [int(x) for x in numbers_list]
print(str_to_int)


