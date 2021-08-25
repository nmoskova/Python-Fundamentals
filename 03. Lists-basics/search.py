n = int(input())
key_word = input()
all_words = []
list_key_words = []

for _ in range(n):
    text = input()
    all_words.append(text)

    if key_word in text:
        list_key_words.append(text)

print(all_words)
print(list_key_words)