followers = {}

while True:
    command = input()

    if command == "Log out":
        break

    command = command.split(": ")
    action = command[0]
    username = command[1]

    if action == "New follower":

        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

    elif action == "Like":
        count = int(command[2])

        if username not in followers:
            followers[username] = {"likes": count, "comments": 0}
        else:
            followers[username]["likes"] += count

    elif action == "Comment":

        if username not in followers:
            followers[username] = {"likes": 0, "comments": 1}
        else:
            followers[username]["comments"] += 1

    elif action == "Blocked":

        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]

print(f"{len(followers)} followers")

for name, data in followers.items():
    followers[name] = data["likes"] + data["comments"]

for name, count in sorted(followers.items(), key=lambda x: (-x[1], x[0])):
    print(f"{name}: {count}")

