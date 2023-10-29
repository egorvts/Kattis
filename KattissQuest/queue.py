import heapq as hq

q1 = []
q2 = q1[:]

hq.heappush(q1, 1)
hq.heappush(q2, 2)

print(q1)
print(q2)
print(type(q1))
print(type(q2))