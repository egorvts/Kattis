n = int(input())
heights = list(map(int, input().split()))
diff = 0

for i in range(n):
    max_diff = 0
    for j in range(i+1, n):
        if heights[j] >= heights[i]:
            if max_diff > diff:
                diff = max_diff
            break
        else:
            d = heights[i] - heights[j]
            if d > max_diff:
                max_diff = d

for i in range(n-1, 0-1, -1):
    max_diff = 0
    for j in range(i-1, 0-1, -1):
        if heights[j] >= heights[i]:
            if max_diff > diff:
                diff = max_diff
            break
        else:
            d = heights[i] - heights[j]
            if d > max_diff:
                max_diff = d

print(diff)
