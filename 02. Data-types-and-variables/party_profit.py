# + 50 coins every day !
# - 2 coins per companion for food !
# every 3rd day - motivational party, - 3 coins per companion for water!
# every 5th day - slay monster boss, + 20 coins per companion !!! if there is motivational party
# the same day -> - 2 coins per companion
# every 10th day at the start of the day!!!  2 of the companions leave!
# every 15th day new 5 people join at the beginning of the day !

party_size = int(input())
days_of_adventure = int(input())
count_companion = party_size
count_coins = 0

for day in range(1, days_of_adventure + 1):
    count_coins += 50

    if day % 10 == 0:
        count_companion -= 2

    if day % 15 == 0:
        count_companion += 5
    count_coins -= count_companion * 2

    if day % 3 == 0:
        count_coins -= count_companion * 3

    if day % 5 == 0:
        count_coins += count_companion * 20

    if day % 3 == 0 and day % 5 == 0:
        count_coins -= count_companion * 2

print(f'{count_companion} companions received {count_coins // count_companion} coins each.')
