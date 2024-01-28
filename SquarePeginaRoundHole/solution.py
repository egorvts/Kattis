from math import sqrt
from collections import deque

n, m, k = map(int, input().split())

plots = list(map(int, input().split()))
circular = list(map(int, input().split()))
square = list(map(lambda x: (x * sqrt(2) / 2), list(map(int, input().split()))))

houses = circular + square

plots.sort(reverse=True)
houses.sort(reverse=True)

plots = deque(plots)
houses = deque(houses)

res = 0
while plots and houses:
    if plots[0] > houses[0]:
        res += 1
        plots.popleft()
    houses.popleft()

print(res)

