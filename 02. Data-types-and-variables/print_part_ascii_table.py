char_index_start = int(input())
char_index_stop = int(input())
sum_ascii = ''

for each_char in range(char_index_start, char_index_stop+1):
    char_to_ascii = chr(each_char)
    sum_ascii += char_to_ascii + ' '

print(sum_ascii)