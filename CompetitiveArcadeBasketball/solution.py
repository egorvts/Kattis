n, p, m = map(int, input().split())
players = dict()
for i in range(n):
    name = input()
    players[name] = 0

for i in range(m):
    name, score = input().split()
    score = int(score)
    players[name] += score

no_wins = True
for player in players.keys():
    if players[player] >= p:
        no_wins = False
        print(player, "wins!")

if no_wins:
    print("No winner!")
