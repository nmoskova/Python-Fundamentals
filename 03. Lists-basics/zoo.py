tail = input()
body = input()
head = input()

# meerkat = [head, body, tail]
meerkat = [tail, body, head]
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]  #swapping elements

print(meerkat)