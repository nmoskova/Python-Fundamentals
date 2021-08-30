def decipher_word(word: str):
    num_to_char = ''
    chars_list = []

    for char in word:
        if char.isnumeric():
            num_to_char += char

        else:
            chars_list.append(char)

    num_to_char = chr(int(num_to_char))
    chars_list.insert(0, num_to_char)
    chars_list[1], chars_list[-1] = chars_list[-1], chars_list[1]

    return "".join(chars_list)


secret_message = input().split()
print(" ".join([decipher_word(each) for each in secret_message]))

