def register(registered_users: dict, user_id: str, licence_plate: str):
    if user_id not in registered_users:
        registered_users[user_id] = licence_plate
        print(f"{user_id} registered {licence_plate} successfully")
    else:
        print(f"ERROR: already registered with plate number {registered_users[user_id]}")


def unregister(registered_users: dict, user_id: str):
    if user_id not in registered_users:
        print(f"ERROR: user {user_id} not found")
    else:
        registered_users.pop(user_id)
        print(f"{user_id} unregistered successfully")


registered_users = {}
num_commands = int(input())

for _ in range(num_commands):
    data = input().split()
    command = data[0]
    user_id = data[1]

    if command == "register":
        licence_plate = data[2]
        register(registered_users, user_id, licence_plate)
    elif command == "unregister":
        unregister(registered_users, user_id)

for key, value in registered_users.items():
    print(f"{key} => {value}")
