command_list = input().split('|')
initial_health = 100
initial_bitcoin = 0
count_rooms = 0
passed_through_all_rooms = True

for each_element in command_list:
    list_each_element = each_element.split(' ')
    command = list_each_element[0]
    number = int(list_each_element[1])

    if command == "potion":

        if (initial_health + number) > 100:
            number = 100 - initial_health
            initial_health = 100
        else:
            initial_health += number

        print(f"You healed for {number} hp.")
        print(f"Current health: {initial_health} hp.")
        count_rooms += 1

    elif command == "chest":
        print(f"You found {number} bitcoins.")
        initial_bitcoin += number
        count_rooms += 1

    else:
        initial_health -= number
        count_rooms += 1

        if initial_health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {count_rooms}")
            passed_through_all_rooms = False
            break
        else:
            print(f"You slayed {command}.")

if passed_through_all_rooms:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoin}")
    print(f"Health: {initial_health}")