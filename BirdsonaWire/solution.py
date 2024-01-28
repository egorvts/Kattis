l, d, n = map(int, input().split())

birds = [6]
for _ in range(n):
    birds.append(int(input()))

# if birds[-1] != l-6:
birds.append(l-6)
birds.sort()

res = 0
for i in range(n+1):
    distance = birds[i+1] - birds[i]
    # print(birds[i], birds[i+1])
    res += distance // d

print(res - n + 1)
