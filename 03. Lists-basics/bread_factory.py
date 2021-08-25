initial_energy = 100
initial_coins = 100
events_list = input().split('|')
bakrupted = False

for event in events_list:
    single_event_list = event.split('-')
    curr_event_or_ingredient = single_event_list[0]
    energy_or_coins = int(single_event_list[1])

    if curr_event_or_ingredient == 'rest':
        energy_gained = energy_or_coins

        if initial_energy + energy_or_coins > 100:
            energy_gained = 100 - initial_energy
        initial_energy += energy_gained
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {initial_energy}.")

    elif curr_event_or_ingredient == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += energy_or_coins
            print(f"You earned {energy_or_coins} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")

    else:
        if initial_coins > energy_or_coins:
            initial_coins -= energy_or_coins
            print(f"You bought {curr_event_or_ingredient}.")
        else:
            print(f"Closed! Cannot afford {curr_event_or_ingredient}.")
            bakrupted = True
            break

if not bakrupted:
    print(f"Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}")
