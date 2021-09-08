words = [w.lower() for w in input().split()]
seq_words = {}

for word in words:
    if word not in seq_words:
        seq_words[word] = 1
    else:
        seq_words[word] += 1

for key, value in seq_words.items():
    if not value % 2 == 0:
        print(f"{key}", end=' ')
