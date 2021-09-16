num_cars = int(input())
cars = {}

for _ in range(num_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}

while True:
    command = input()

    if command == "Stop":
        break

    data = command.split(" : ")
    action = data[0]
    car = data[1]

    if action == "Drive":
        distance = int(data[2])
        fuel = int(data[3])

        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]

    elif action == "Refuel":
        fuel = int(data[2])
        maximum_fuel = 75

        if not (cars[car]["fuel"] + fuel) > maximum_fuel:
            cars[car]["fuel"] += fuel
        else:
            fuel = maximum_fuel - cars[car]["fuel"]
            cars[car]["fuel"] = maximum_fuel

        print(f"{car} refueled with {fuel} liters")

    elif action == "Revert":
        km = int(data[2])
        cars[car]["mileage"] -= km

        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {km} kilometers")

sorted_cars = sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0]))

for car, data in sorted_cars:
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")



