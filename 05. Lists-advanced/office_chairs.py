rooms = int(input())
free_chairs = 0
enough_free_chairs = True

for room in range(1, rooms+1):
    chairs, visitors = input().split(" ")
    chairs, visitors = len(chairs), int(visitors)

    if visitors > chairs:
        enough_free_chairs = False
        print(f"{visitors - chairs} more chairs needed in room {room}")

    else:
        free_chairs += (chairs - visitors)


if enough_free_chairs:
    print(f"Game On, {free_chairs} free chairs left")