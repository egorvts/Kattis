import math as m

n, k = map(int, input().split())
requests = [0] * 101_001

for t in range(n):
    inp = int(input())
    requests[inp] += 1
    requests[inp+1000] -= 1

max_requests = 0
requests_count = 0

for i in range(len(requests)):
    requests_count += requests[i]
    max_requests = max(requests_count, max_requests)

# for i in range(1, m.ceil(requests[-1]/1000)*1000, 1000):
#     one_time_requests = 0
#     for j in range(len(requests)):
#         if requests[j] < i:
#             one_time_requests += 1
#         else:
#             requests = requests[j:]
#     max_requests = max(max_requests, one_time_requests)

# for i in range(1000, 100_000+1, 1000):
#     one_time_requests = 0
#     for j in requests:
#         if j < i:
#             one_time_requests += 1
#             requests.pop(0)
#         else:
#             break
#     if one_time_requests > max_requests:
#         max_requests = one_time_requests

print(m.ceil(max_requests / k))
