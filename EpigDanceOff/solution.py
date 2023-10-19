n, m = map(int, input().split())

moves = [[[]] * m] * n

for i in range(n):
    moves[i] = list(input())

count = 0

for i in range(m):
    for j in range(n):
        if moves[j][i] != "_":
            break
    else:
        count += 1

print(count + 1)
