n = int(input())
q = list(map(int, input().split()))

m = 0
ind_m = 0
for i in range(n):
    if q.count(q[i]) != 1:
        continue
    elif q[i] > m:
        m = q[i]
        ind_m = i

if m == 0:
    print("none")
else:
    print(ind_m+1)
