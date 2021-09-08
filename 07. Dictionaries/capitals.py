country_names = input().split(", ")
capitals = input().split(", ")

count_cap_dict = dict(zip(country_names, capitals))

for country, capital in count_cap_dict.items():
    print(f"{country} -> {capital}")