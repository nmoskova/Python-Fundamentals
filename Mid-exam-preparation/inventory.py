collect_item_list = input().split(', ')
command = input()

while command != "Craft!":
    command = command.split(' - ')
    action = command[0]
    item = command[1]

    if (action == 'Collect') and (item not in collect_item_list):
        collect_item_list.append(item)

    elif action == 'Drop' and item in collect_item_list:
        collect_item_list.remove(item)

    elif action == 'Renew' and item in collect_item_list:
        collect_item_list.remove(item)
        collect_item_list.append(item)

    elif action == 'Combine Items':
        item = item.split(':')
        old_item = item[0]
        new_item = item[1]

        if old_item in collect_item_list:
            index_old_item = collect_item_list.index(old_item)
            collect_item_list.insert(index_old_item+1, new_item)

    command = input()

print(', '.join(collect_item_list))