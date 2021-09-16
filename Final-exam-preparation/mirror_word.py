import re

text = input()
pattern = r"(?P<delimiter>@|#)(?P<word_one>[A-Za-z]{3,})(?P=delimiter){2}(?P<word_two>[A-Za-z]{3,})(?P=delimiter)"

valid_pairs = len(re.findall(pattern, text))

if valid_pairs > 0:
    print(f"{valid_pairs} word pairs found!")
else:
    print("No word pairs found!")

mirror_words = []

for match in re.finditer(pattern, text):
    word_one = match.group("word_one")
    word_two = match.group("word_two")

    if word_one[::-1] == word_two:
        mirror_words.append(f"{word_one} <=> {word_two}")

if len(mirror_words) > 0:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")

