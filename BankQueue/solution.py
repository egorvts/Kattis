n, t = map(int, input().split())
people = {}
for i in range(n):
    c, time = map(int, input().split())
    if time in people:
        if people[time] < c:
            people[time] = c
    else:
        people[time] = c

lst = []
for p in people:
    lst.append((p, people[p]))
lst.sort(key=lambda x: x[0])

res = 0
for i in range(t):
    if not lst:
        break
    p = lst.pop(0)
    res += p[1]

print(res)
