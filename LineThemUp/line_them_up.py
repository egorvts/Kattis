people_count = int(input())
distance = list(map(int, input().split()))

order = [1]
for d in range(len(distance)):
    order.append(distance.index(d) + 2)

print(*order)
