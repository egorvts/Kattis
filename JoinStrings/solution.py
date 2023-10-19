n = int(input())
strings = []

for _ in range(n):
    strings.append(input())

queue: list = list(range(1, n+1))
for _ in range(n-1):
    # print(strings)
    i1, i2 = map(int, input().split())
    print(i1, i2)
    queue[i1-1] = [queue[i1-1]] + [i2]

print(queue)
