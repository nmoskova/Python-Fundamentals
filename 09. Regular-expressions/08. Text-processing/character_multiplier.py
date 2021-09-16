string_1, string_2 = input().split()
total_sum = 0
min_lenght = min(len(string_1), len(string_2))
max_lenght = max(len(string_1), len(string_2))
max_string = max(string_1, string_2, key=len)


if not len(string_1) == len(string_2):

    for i in range(min_lenght):
        total_sum += (ord(string_1[i]) * ord(string_2[i]))

    for i in range(min_lenght, max_lenght):
        total_sum += ord(max_string[i])

else:

    for i in range(len(string_1)):
        total_sum += (ord(string_1[i]) * ord(string_2[i]))

print(total_sum)


