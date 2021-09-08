players = {}
command = input()
duel = False

while not command == "Season end":
    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)

        if player not in players:
            players[player] = {position: skill}

        else:
            if position not in players[player]:
                players[player].update({position: skill})
            else:
                if players[player][position] < skill:
                    players[player][position] = skill

    else:
        player_1, player_2 = command.split(" vs ")

        if (player_1 and player_2) in players:
            for pos, ski in players[player_1].items():
                if pos in players[player_2]:
                    duel = True
        if duel:
            total_player_1 = sum(players[player_1].values())
            total_player_2 = sum(players[player_2].values())

            if total_player_1 == total_player_2:
                duel = False
                command = input()
                continue
            elif total_player_1 < total_player_2:
                players.pop(player_1)
            else:
                players.pop(player_2)

    duel = False
    command = input()

totals = {p: sum(d.values()) for p, d in players.items()}
sorted_totals = dict(sorted(totals.items(), key=lambda x: (-x[1], x[0])))

for pl, sk in sorted_totals.items():
    print(f"{pl}: {sk} skill")
    player_sorted = dict(sorted(players[pl].items(), key=lambda x: (-x[1], x[0])))
    for pos, skill in player_sorted.items():

        print(f"- {pos} <::> {skill}")