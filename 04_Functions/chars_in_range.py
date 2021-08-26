def chars(char1, char2):
    some_string = ''

    for each in range(ord(char1)+1, ord(char2)):

        some_string += chr(each) + ' '

    return some_string


first = input()
second = input()

print(chars(first, second))