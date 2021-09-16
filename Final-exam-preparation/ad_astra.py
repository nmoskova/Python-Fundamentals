import re

pattern = r"(?P<split>#|\|)(?P<item_name>[A-Za-z\s]+)(?P=split)(?P<date>\d{2}\/\d{2}\/\d{2})(?P=split)(?P<calories>\d+)(?P=split)"
text = input()
total_calories = 0

for match in re.finditer(pattern, text):
    total_calories += int(match.group("calories"))

days_last = total_calories // 2000


print(f"You have food to last you for: {days_last} days!")

for match in re.finditer(pattern, text):
    item_name = match.group("item_name")
    exp_date = match.group("date")
    calories = match.group("calories")
    print(f"Item: {item_name}, Best before: {exp_date}, Nutrition: {calories}")