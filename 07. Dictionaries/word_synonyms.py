num_lines = int(input())
dicts = {}

for _ in range(num_lines):
    key = input()
    value = input()

    if key not in dicts:
        dicts[key] = []
    dicts[key].append(value)

for word, synonyms in dicts.items():
    print(f"{word} - {', '.join(synonyms)}")