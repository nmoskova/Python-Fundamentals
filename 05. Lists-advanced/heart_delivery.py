def index_in_range(neighborhood: list, index):

    if neighborhood[index] == 0:
        print(f"Place {index} already had Valentine's day.")

    else:
        neighborhood[index] -= 2
        if neighborhood[index] == 0:
            print(f"Place {index} has Valentine's day.")


neighborhood = [int(x) for x in input().split("@")]
index = 0
command = input()

while not command == "Love!":
    jump_lenght = int((command.split())[1])
    index += jump_lenght

    if index in range(len(neighborhood)):
        index_in_range(neighborhood, index)

    else:
        index = 0
        index_in_range(neighborhood, index)

    command = input()


print(f"Cupid's last position was {index}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")

else:
    while 0 in neighborhood:
        neighborhood.remove(0)
    print(f"Cupid has failed {len(neighborhood)} places.")