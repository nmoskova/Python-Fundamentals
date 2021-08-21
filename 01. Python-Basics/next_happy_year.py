year = int(input()) + 1

while not len(str(year)) == len(set(str(year))):
    year += 1

print(year)
