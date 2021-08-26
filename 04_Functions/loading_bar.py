def loading_bar(number):
    digit = number // 10
    loading_list = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    percentage_list = []

    for each_dot in range(1, digit + 1):
        loading_list.remove('.')
        percentage_list.append('%')

    list_for_print = percentage_list + loading_list
    return list_for_print


number = int(input())

if number == 100:
    print('100% Complete!')
    print('[%%%%%%%%%%]')
else:
    print(f'{number}%', end=' ')
    print(f"""[{''.join(loading_bar(number))}]""")
    print('Still loading...')
