n = int(input())
order = list(map(int, input().split()))
sorted_order = list(map(int, input().split()))

visited = [False] * n
visited2 = [False] * n

parity1 = 0
parity2 = 0

for i in range(n):
    if not visited[i]:
        count = 1
        visited[i] = True
        while True:
            j = order[i] - 1
            if visited[j]:
                break
            else:
                count += 1
                visited[j] = True
                i = order[j] - 1
                if visited[i]:
                    break
                else:
                    visited[i] = True
                    count += 1

        # print("1:", count)
        parity1 = (parity1 + (count - 1) % 2) % 2

# print(parity1)

for i in range(n):
    if not visited2[i]:
        count = 1
        visited2[i] = True
        while True:
            j = sorted_order[i] - 1
            if visited2[j]:
                break
            else:
                count += 1
                visited2[j] = True
                i = sorted_order[j] - 1
                if visited2[i]:
                    break
                else:
                    visited2[i] = True
                    count += 1

        # print("1:", count)
        parity2 = (parity2 + (count - 1) % 2) % 2

# print(parity2)

if parity1 == parity2:
    print("Possible")
else:
    print("Impossible")
