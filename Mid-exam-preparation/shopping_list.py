def urgent(item: str, shopping_list: list):
    if item not in shopping_list:
        shopping_list.insert(0, item)


def unnecessary(item: str, shopping_list: list):
    if item in shopping_list:
        shopping_list.remove(item)


def correct(old_item: str, new_item: str, shopping_list: list):
    if old_item in shopping_list:
        index = shopping_list.index(old_item)
        shopping_list[index] = new_item


def rearrange(item: str, shopping_list: list):
    if item in shopping_list:
        shopping_list.append(item)
        shopping_list.remove(item)


shopping_list = input().split("!")
command = input()

while not command == "Go Shopping!":

    if "Correct" in command:
        action, old_item, new_item = command.split()
    else:
        action, item = command.split()

    if action == "Urgent":
        urgent(item, shopping_list)
    elif action == "Unnecessary":
        unnecessary(item, shopping_list)
    elif action == "Correct":
        correct(old_item, new_item, shopping_list)
    elif action == "Rearrange":
        rearrange(item, shopping_list)
    command = input()

print(*shopping_list, sep=", ")



