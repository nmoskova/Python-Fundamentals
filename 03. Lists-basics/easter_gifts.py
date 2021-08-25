gifts_list = input().split()
command = input()

while not command == "No Money":

    command_to_list = command.split()

    if "OutOfStock" in command:
        to_change = command_to_list[1]
        for i in range(len(gifts_list)):
            if gifts_list[i] == to_change:
                gifts_list[i] = 'None'

    elif "Required " in command:
        i = int(command_to_list[2])
        if 0 < i < len(gifts_list):
            gifts_list[i] = command_to_list[1]

    elif "JustInCase" in command:
        gifts_list[-1] = command_to_list[1]
    command = input()

while 'None' in gifts_list:
    gifts_list.remove('None')

list_to_string = ' '.join(gifts_list)
print(list_to_string)
