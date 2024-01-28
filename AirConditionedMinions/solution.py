n = int(input())
temps = [0] * (2*n + 1)
minions = []
for _ in range(n):
    min_t, max_t = map(int, input().split())
    minions.append([min_t, max_t])
    for t in range(min_t, max_t+1):
        temps[t] += 1

# rooms = 0
# while minions:
#     best_t = temps.index(max(temps))
#     left = []
#     for m in range(len(minions)):
#         if minions[m][0] <= best_t <= minions[m][1]:
#             for i in range(minions[m][0], minions[m][1]+1):
#                 temps[i] -= 1
#         else:
#             left.append(minions[m])
#     rooms += 1
#     minions = left
# print(rooms)
