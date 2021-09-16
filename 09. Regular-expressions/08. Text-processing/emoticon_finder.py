text = input()
i = 0

while i < len(text):

    if text[i] == ":":
        emoticon = text[i] + text[i+1]
        print(emoticon)

    i += 1