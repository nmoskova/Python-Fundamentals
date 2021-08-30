def collect(items_list: list, item: str):
    if item not in items_list:
        items_list.append(item)


def drop(items_list: list, item: str):
    if item in items_list:
        items_list.remove(item)


def combine_items(items_list: list, old_item: str, new_item: str):
    if old_item in items_list:
        items_list.insert(items_list.index(old_item)+1, new_item)


def renew(items_list: list, item: str):
    if item in items_list:
        items_list.append(item)
        items_list.remove(item)


items_list = input().split(", ")
command = input()

while not command == "Craft!":
    action, item = command.split(" - ")

    if "Combine" in action:
        old_item, new_item = item.split(":")

    if action == "Collect":
        collect(items_list, item)

    elif action == "Drop":
        drop(items_list, item)

    elif action == "Combine Items":
        combine_items(items_list, old_item, new_item)

    elif action == "Renew":
        renew(items_list, item)
    command = input()

print(*items_list, sep=", ")

