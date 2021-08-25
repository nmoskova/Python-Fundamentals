team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
game_is_terminated = False
sequence_cards = input()
cards_to_list = sequence_cards.split(' ')

for card in cards_to_list:
    if len(team_a) < 7 or len(team_b) < 7:
        game_is_terminated = True
        break

    if card in team_a:
        team_a.remove(card)

    elif card in team_b:
        team_b.remove(card)

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_is_terminated:
    print('Game was terminated')

# team_a = 11
# team_b = 11
# game_is_terminated = False
# sequence_cards = input()
# cards_to_list = sequence_cards.split(' ')
# unique_list = list(set(cards_to_list))
# for each_card in unique_list:
#     if team_a < 7 or team_b < 7:
#         game_is_terminated = True
#         break
#     if 'A' in each_card:
#         team_a -= 1
#     elif 'B' in each_card:
#         team_b -= 1
# print(f"Team A - {team_a}; Team B - {team_b}")
# if game_is_terminated:
#     print('Game was terminated')
