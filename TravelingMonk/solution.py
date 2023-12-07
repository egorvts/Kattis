a, d = map(int, input().split())
ascent = []
descent = []

total_distance = 0
total_time = 0

for _ in range(a):
    h, t = map(float, input().split())
    total_time += t
    total_distance += h
    ascent.append([h, t])

for _ in range(d):
    h, t = map(float, input().split())
    descent.append([h, t])


def ascenting(asc, time):
    complited_time = 0
    distance = 0
    for s in asc:
        if (complited_time < time) and ((s[1] + complited_time) < time):
            distance += s[0]
            complited_time += s[1]
        else:
            distance += (s[0]/s[1] * (time - complited_time))
            return distance
    return distance


def descenting(des, time):
    complited_time = 0
    distance = 0
    for s in des:
        if (complited_time < time) and ((s[1] + complited_time) < time):
            distance += s[0]
            complited_time += s[1]
        else:
            distance += (s[0]/s[1] * (time - complited_time))
            return total_distance - distance
    return total_distance - distance


min = 0
max = total_time
mid = 0

while mid != (min + max) / 2:
    mid = (min + max) / 2
    asc = ascenting(ascent, mid)
    des = descenting(descent, mid)

    if asc == des:
        max = mid
    elif asc < des:
        min = mid
    elif asc > des:
        max = mid

print("%.5f"%mid)
