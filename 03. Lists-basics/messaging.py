code = input().split()
string_to_list = [x for x in input()]
message = []

for symbol in code:
    char = [int(x) for x in symbol]

    if len(string_to_list) < sum(char)+1:
        multiplier = (sum(char) // len(string_to_list))
        index = (sum(char) - (multiplier * len(string_to_list)))

    else:
        index = sum(char)

    message.append(string_to_list[index])
    string_to_list.pop(index)

print("".join(message))

