seq_of_str = input().split()
new_str = ""

for word in seq_of_str:
    new_str += word * len(word)

print(new_str)