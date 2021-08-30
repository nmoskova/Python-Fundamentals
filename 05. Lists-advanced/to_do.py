notes = input()
importance_list = [0] * 10

while not notes == "End":
    importance, action = notes.split("-")
    curr_index = int(importance) - 1
    importance_list[curr_index] = action

    notes = input()

print([el for el in importance_list if not el == 0])