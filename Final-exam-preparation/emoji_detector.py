import re

pattern_emoticons = r"(?P<emoji>(?P<start_end>\:\:|\*\*)(?P<emoticon_name>[A-Z][a-z]{2,})(?P=start_end))"
pattern_cool_treshold = r"\d"
text = input()
found_emoticons = []
total_coolness = 1
cool_emojis = []

coolness = [int(num) for num in re.findall(pattern_cool_treshold, text)]
for num in coolness:
    total_coolness *= num

emoticons = re.finditer(pattern_emoticons, text)
for emot in emoticons:
    found_emoticons.append(emot.group("emoji"))

for emot in found_emoticons:
    ch_total = 0

    for ch in emot:

        if not ch == "*" and not ch == ":":
            ch_total += ord(ch)

    if ch_total > total_coolness:
        cool_emojis.append(emot)

print(f"Cool threshold: {total_coolness}")
print(f"{len(found_emoticons)} emojis found in the text. The cool ones are:")
[print(emoji) for emoji in cool_emojis]



