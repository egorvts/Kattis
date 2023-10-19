n = int(input())
guests = list(map(int, input().split()))
distances = {}

for i in range(n):
    if guests[i] in distances:
        if len(distances[guests[i]]) == 1:
            distances[guests[i]].append(i)
        else:
            if (distances[guests[i]][1] - distances[guests[i]][0]) > (i - distances[guests[i]][1]):
                distances[guests[i]] = [distances[guests[i]][1], i]
    else:
        distances[guests[i]] = [i]

min_distance = n
for d in distances.values():
    if (len(d) == 2) and ((d[1] - d[0]) < min_distance):
        min_distance = d[1] - d[0]

print(min_distance)
