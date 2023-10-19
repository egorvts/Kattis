n = int(input())
at_bats = list(map(int, input().split()))[:n]

at_bats_count = 0
points = 0

for i in at_bats:
    if i != -1:
        at_bats_count += 1
        points += i
    elif i == 0:
        at_bats_count += 1
    else:
        continue

print(points/at_bats_count)
