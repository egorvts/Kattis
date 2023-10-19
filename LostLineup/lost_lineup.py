team = []

for _ in range(int(input())):
    team.append(input())

if sorted(team) == team:
    print("INCREASING")
elif sorted(team, reverse=True) == team:
    print("DECREASING")
else:
    print("NEITHER")
