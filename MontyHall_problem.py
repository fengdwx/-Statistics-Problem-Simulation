import random

# simulate the three doors
doors = [False, False, False]

wins = 0
loses = 0

times = 1000000

for i in range(times):
    doors[random.randint(0, 2)] = True

    # player chooses a door
    player_choice = random.randint(0, 2)

    # host reveals a door that is not chosen by the player and does not contain the prize
    for j in range(3):
        if j != player_choice and not doors[j]:
            host_reveal = j
            break

    # player switches to the other unopened door
    for j in range(3):
        if j != player_choice and j != host_reveal:
            player_choice = j
            break

    # check if player wins
    if doors[player_choice]:
        wins += 1
    else:
        loses += 1

    doors = [False, False, False]

print("Win probability: ", wins/times)
print("Lose probability: ", loses/times)

