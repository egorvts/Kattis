r, c = map(int, input().split())
map = []
for i in range(r):
    map.append(list(input()))

counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
for i in range(r-1):
    for j in range(c-1):
        space = [map[i][j], map[i+1][j], map[i][j+1], map[i+1][j+1]]

        if "#" not in space:
            counts[space.count("X")] += 1

for c in counts:
    print(counts[c])

