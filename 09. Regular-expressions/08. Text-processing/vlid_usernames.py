usernames = [un for un in input().split(", ") if len(un) in range(3, 17)]

for un in usernames[::-1]:

    for ch in un:
        if not (ch.isalnum() or ch == "-" or ch == "_"):
            usernames.remove(un)
            break

for un in usernames:
    print(un)