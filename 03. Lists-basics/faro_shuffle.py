cards_to_shuffle = input().split(' ')
times_to_shuffle = int(input())
half_size_list = (len(cards_to_shuffle)) // 2
shuffled_list = cards_to_shuffle

for _ in range(times_to_shuffle):
    new_list = []
    left_list = shuffled_list[0:half_size_list]
    right_list = shuffled_list[half_size_list:]

    for i in range(half_size_list):
        new_list.append(left_list[i])
        new_list.append(right_list[i])

    shuffled_list = new_list

print(shuffled_list)
