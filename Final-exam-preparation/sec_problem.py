import re

pattern = r"(?P<delim>U\$)(?P<username>[A-Z][a-z]{2,})(?P=delim)(?P<sec_delim>P\@\$)(?P<password>[A-Za-z]{5,}\d+)(?P=sec_delim)"

n = int(input())
count = 0

for _ in range(n):
    text = input()

    matches = re.match(pattern, text)

    if matches:
        count += 1
        username = matches.group("username")
        password = matches.group("password")
        print("Registration was successful")
        print(f"Username: {username}, Password: {password}")

    else:
        print("Invalid username or password")

print(f"Successful registrations: {count}")