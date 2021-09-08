data = input()
results = {}
submission = {}

while not data == "exam finished":
    command = data.split("-")

    if command[1] == "banned":
        username = command[0]

        for l, data in results.items():
            if username in data:
                results[l].pop(username)
    else:
        username, language, points = command
        points = int(points)

        if language not in results:
            results[language] = {username: points}

        if username in results[language]:
            if points > results[language][username]:
                results[language][username] = points
        else:
            results[language].update({username: points})

        if language in submission:
            submission[language] += 1
        else:
            submission[language] = 1

    data = input()

res_by_un = {}

for l, d in results.items():
    for un, p in d.items():
        if un in res_by_un:
            if res_by_un[un] < p:
                res_by_un[un] = p
        else:
            res_by_un[un] = p

print("Results:")
for name, points in sorted(res_by_un.items(), key=lambda x: (-x[1], x[0])):
    print(f"{name} | {points}")

print("Submissions:")
for (language, subm) in sorted(submission.items(), key=lambda x: (-x[1], x[0])):
    print(f"{language} - {subm}")



