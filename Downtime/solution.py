import math as m

n, k = map(int, input().split())
requests = []

for t in range(n):
    requests.append(int(input()))

max_requests = 0

for i in range(len(requests)):
    one_time_requests = []
    for j in range(len(requests)):
        if (i != j) and (requests[i] - requests[j] < 1000):
            one_time_requests.append(requests[j])
    if len(one_time_requests) > max_requests:
        max_requests = len(one_time_requests)

print(m.ceil(max_requests / k))
    