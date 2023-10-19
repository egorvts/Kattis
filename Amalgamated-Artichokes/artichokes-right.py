import math as m

p, a, b, c, d, n = map(int, input().split())
prices = []
diffs = []
decline = 0

for k in range(1, n + 1):
    prices.append(p * (m.sin(a * k + b) + m.cos(c * k + d) + 2))

maxPrice = 0
maxDiff = 0

for i in range(0, len(prices)):
    if prices[i] > maxPrice:
        maxPrice = prices[i]
    if maxPrice - prices[i] > maxDiff:
        maxDiff = maxPrice - prices[i]

print(maxDiff)
