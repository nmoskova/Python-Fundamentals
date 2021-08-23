key = int(input())
number_letters = int(input())
word = ''

for each_letter in range(1, number_letters + 1):
    letter = ord(input())
    new_letter = chr(letter + key)
    word += new_letter

print(word)
