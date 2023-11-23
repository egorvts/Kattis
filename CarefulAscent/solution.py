x, y = map(int, input().split())
zones = [y]
shields = []
for i in range(int(input())):
    l, u, f = map(int, input().split())
    zones.append(l)
    zones.append(u)
    shields.append(f)

zones.sort()

for i in range(len(zones)-1):
    if i == 0:
        y_change = zones[i]
    else:
        y_change = zones[i] - zones[i-1]
