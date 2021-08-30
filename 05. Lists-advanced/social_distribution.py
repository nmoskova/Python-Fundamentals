population = [int(el) for el in input().split(", ")]
minimum_wealth = int(input())
enough_wellness = True


for i in range(len(population)):
    citizen = population[i]

    if citizen < minimum_wealth:
        wealthiest = max(population)

        if (wealthiest - (minimum_wealth - citizen)) >= minimum_wealth:

            population[i] = minimum_wealth
            wealthiest_index = population.index(wealthiest)
            wealthiest -= (minimum_wealth - citizen)
            population[wealthiest_index] = wealthiest

        else:
            print("No equal distribution possible")
            enough_wellness = False
            break

if enough_wellness:
    print(population)