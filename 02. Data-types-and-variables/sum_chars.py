number_lines = int(input())
total_sum = 0

for each_char in range(1, number_lines+1):
    char = input()
    char_ascii = ord(char)
    total_sum += char_ascii

print(f'The sum equals: {total_sum}')