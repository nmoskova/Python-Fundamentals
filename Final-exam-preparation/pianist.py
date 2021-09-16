num_pieces = int(input())
pieces = {}

for _ in range(num_pieces):
    piece, composer, key = input().split("|")
    pieces[piece] = {"composer": composer, "key": key}

while True:
    command = input()

    if command == "Stop":
        break

    command = command.split("|")
    action = command[0]
    piece = command[1]

    if action == "Add":
        composer, key = command[2], command[3]

        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":

        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command[2]

        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1]["composer"]))

for piece, data in sorted_pieces:
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")


