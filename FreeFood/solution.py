n = int(input())

free_food = set()
for i in range(n):
    s, t = map(int, input().split())
    for i in range(s, t+1):
        free_food.add(i)

print(len(free_food))
