n, b = map(int, input().split())
a = list(map(int, input().split()))

m = 0
for i in range(n):
    if a[i] == b:
        m = i

d = dict()
d[0] = 1
sum = 0

for i in range(m+1, n):
    if a[i] > a[m]:
        sum += 1
    else:
        sum -= 1
    if sum in d:
        d[sum] += 1
    else:
        d[sum] = 1

sum = 0
ans = d[0]
for i in range(m-1, -1, -1):
    if a[i] > a[m]:
        # print("+", a[i])
        sum += 1
    else:
        # print("-", a[i])
        sum -= 1
    if (-1 * sum) in d:
        ans += d[(-1 * sum)]

print(ans)
