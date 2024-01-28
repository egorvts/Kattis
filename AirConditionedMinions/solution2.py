n = int(input())
minions = []
for _ in range(n):
    minions.append(list(map(int, input().split())))

minions.sort(key=lambda x: x[1])

rooms = 1

temp = minions[0][1]
for t in minions[1:]:
    if t[0] > temp:
        rooms += 1
        temp = t[1]

print(rooms)