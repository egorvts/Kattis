n = int(input())
temps = [0] * (2*n + 1)
minions = []
for _ in range(n):
    min_t, max_t = map(int, input().split())
    minions.append([min_t, max_t])
    for t in range(min_t, max_t+1):
        temps[t] += 1
