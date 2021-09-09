def check_password(p):
    result = []
    count_characters = len(p)
    count_digits = 0

    if count_characters not in range(6, 11):
        result.append("Password must be between 6 and 10 characters")

    for symbol in p:
        symbol_check = ord(symbol)

        if symbol_check in range(48, 58) or symbol_check in range(65, 91) or symbol_check in range(97, 123):
            pass
        else:
            result.append("Password must consist only of letters and digits")
            break

    for symbol in p:
        symbol_check = ord(symbol)

        if 48 <= symbol_check <= 58:
            count_digits += 1

    if count_digits < 2:
        result.append("Password must have at least 2 digits")
    return result


password = input()

if check_password(password) == []:
    print('Password is valid')
else:
    for each_line in check_password(password):
        print(each_line)

