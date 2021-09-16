n = int(input())

cars = {}

for x in range(n):
    car, mileage, fuel = input().split("|")
    cars[car] = car
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

command = input()
while not command == "Stop":
    command = command.split(" : ")

    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        gas = int(command[3])

        if cars[car]["fuel"] < gas:
            print("Not enough fuel to make that ride")
        else:
            print(f"{car} driven for {distance} kilometers. {gas} liters of fuel consumed.")
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= gas

        if cars[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]

    elif command[0] == "Refuel":
        car = command[1]
        gas = int(command[2])

        if cars[car]["fuel"] + gas > 75:
            print(f"{car} refueled with {75 - cars[car]['fuel']} liters")
            cars[car]["fuel"] = 75
        else:
            print(f"{car} refueled with {gas} liters")
            cars[car]["fuel"] += gas

    elif command[0] == "Revert":
        car = command[1]
        kilometers = int(command[2])

        if cars[car]["mileage"] - kilometers < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

sorted_cars = sorted(cars.items(), key=lambda tkvp: (-tkvp[1]["mileage"], tkvp[0]))

for car, data in sorted_cars:
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")