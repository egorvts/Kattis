n = int(input())
order = list(map(int, input().split()))
sorted_order = list(map(int, input().split()))

order_count = 0
sorted_count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if order[i] > order[j]:
            order_count += 1
        if sorted_order[i] > sorted_order[j]:
            sorted_count += 1

if order_count % 2 == sorted_count % 2:
    print("Possible")
else:
    print("Impossible")
