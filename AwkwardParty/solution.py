n = int(input())
guest = list(map(int, input().split()))
min_distance = n
for i in range(n):
    distance = 1
    for j in range(i+1, n):
        if guest[i] == guest[j]:
            if distance < min_distance:
                min_distance = distance
                break
        else:
            distance += 1

print(min_distance)