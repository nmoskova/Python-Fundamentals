some_string = input()
chars_dict = {}

for char in some_string:
    if char not in chars_dict:
        chars_dict[char] = 0
    chars_dict[char] += 1

for char, count in chars_dict.items():
    if not char == " ":
        print(f"{char} -> {count}")
