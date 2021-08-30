wagons = int(input())
wagons_list = [0] * wagons
command = input()

while not command == "End":
    command_list = command.split()

    if command_list[0] == "add":
        wagons_list[-1] += int(command_list[1])

    elif command_list[0] == "insert":
        index, people = int(command_list[1]), int(command_list[2])
        wagons_list[index] += people

    elif command_list[0] == "leave":
        index, people = int(command_list[1]), int(command_list[2])
        wagons_list[index] -= people

    command = input()

print(wagons_list)