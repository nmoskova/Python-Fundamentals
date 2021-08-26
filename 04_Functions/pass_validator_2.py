def len_characters(password):
    if len(password) in range(6, 11):
        return True

    return False


def count_digits(password):
    digits_count = 0

    for ch in password:
        if ch.isdigit():
            digits_count += 1

    if digits_count >= 2:
        return True
    else:
        return False


def is_password_valid(password):
    is_valid = True
    if not len_characters(password):
        is_valid = False
        print("Password must be between 6 and 10 characters")

    if not alphanum:
        is_valid = False
        print("Password must consist only of letters and digits")

    if not count_digits(password):
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")


password = input()
alphanum = password.isalnum()
is_password_valid(password)
