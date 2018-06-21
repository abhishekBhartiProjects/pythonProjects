#!/bin/python3
from random import choice

players = []
file = open('players.txt')
players = file.read().splitlines()

teamA = []
teamB = []

while (len(players) > 0):
    playerA = choice(players)

    teamA.append(playerA)
    players.remove(playerA)

    if players == []:
        break

    playerB = choice(players)

    teamB.append(playerB)
    players.remove(playerB)

print('teamA :', teamA)
print('teamB :', teamB)