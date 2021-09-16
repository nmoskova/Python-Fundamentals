efficiency_first_per_hour = int(input())
efficiency_second_per_hour = int(input())
efficiency_third_per_hour = int(input())
people_count = int(input())
hours_needed = 0

answered_people_by_hour = efficiency_first_per_hour + efficiency_second_per_hour + efficiency_third_per_hour

while people_count > 0:
    hours_needed += 1

    if not hours_needed % 4 == 0:
        people_count -= answered_people_by_hour

print(f"Time needed: {hours_needed}h.")