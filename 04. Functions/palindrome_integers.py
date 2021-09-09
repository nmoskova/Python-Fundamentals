def palindrome(m):
    m_to_list = m.split(', ')
    result = []

    for each_num in m_to_list:
        backward_num = ''
        end_range = -(len(each_num) + 1)

        for index in range(-1, end_range, -1):
            backward_num += str(each_num[index])

        if backward_num == each_num:
            result.append('True')
        else:
            result.append('False')

    return result


nums_to_check = input()

for each in palindrome(nums_to_check):
    print(each)
